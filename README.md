1. Chatinterface: project để kết nối với chatbot engine và public ra người dùng cuối
2. VIBbankchatbotEngine: Project chính (tác giả gọi là bot engine) được xây dựng demo trên nền RASA core và Rasa X
      - Thư mục: /data  là nơi lưu trữ các dữ liệu phục vụ train/test cho project
      - Thư mục: /model là nơi mô hình sau khi được huấn luyện sẽ được lưu trữ tại đây
      - Thư mục: /result là nơi lưu một vài kết quả sau khi huấn luyện
      - file domain.yml là file mãu dữ liệu được khai báo để lưu trữ các câu phản hồi mẫu mà chatbot sẽ phản hồi, ngoài ra lưu trữ các thiết lập tag intent, slot...
      - file action.py là file định nghĩa các custom action
3. VirtualCorebankDB.bak: là file cơ sở dữ liệu giả lập hệ thống ngân hàng lõi corebanking => phục vụ demo khả năng kết nối giữa bot engine và corebank
4. VirtualCorbankAPI: là thư mục project được xây dựng để public webservices dạng API kết nối đến corebank