# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:01:18 2019

@author: norma
"""
print("=====Split hai xấu ký tự==========================================================")
docA = "hạn mức thẻ tín dụng"
docB = "mức chi tiêu tối đa thẻ tín dụng"

bowA = docA.split(" ")
bowB = docB.split(" ")

print(bowB)
print(bowA)
wordSet = set(bowA).union(set(bowB))
print("===============================================================")
print(wordSet)

wordDictA = dict.fromkeys(wordSet, 0) 
wordDictB = dict.fromkeys(wordSet, 0)
print("======Danh sách các từ=========================================================")
print(wordDictA)
print(wordDictB)

for word in bowA:
    wordDictA[word]+=1
    
for word in bowB:
    wordDictB[word]+=1
    

print("======Danh sách các từ 2=========================================================")
     
print(wordDictA)    
print(wordDictB) 

import pandas as pd
print("======DataFrame=========================================================")

print(pd.DataFrame([wordDictA, wordDictB]))


def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)
print("======Tính TF=========================================================")

print(tfBowA)
print(tfBowB)

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict
    
idfs = computeIDF([wordDictA, wordDictB])
print("========Tính IDF==================")
print(idfs)


def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)
print("===============================================================")
import pandas as pd
pd.DataFrame([tfidfBowA, tfidfBowB])

print(pd.DataFrame([tfidfBowA, tfidfBowB]))

