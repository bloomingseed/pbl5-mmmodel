# Giới thiệu
## What: 
- Thống kê số người khiếm thị ở thế giới và việt nam.
- Với sự phát triển của công nghệ, nhiều thiết bị đã được phát triển để hỗ trợ người khiếm thị. Nay với sự phát triển mạnh của trí tuệ nhân tạo hay học máy nói riêng
- Giải pháp cổ điển:
  - gậy dò đường.
    - Chiều dài có hạn, không thể phát hiện được vật thể di chuyển nhanh
    - Khó hoặc không thể nhận diện chính xác nhiều loại vật thể.
  - người giúp đỡ:
    - Không thể luôn có mặt
- Cần một giải pháp thông minh, chính xác hơn.
- Các giải pháp trước đó
    - Quốc tế
    - Trong nước
- Các công trình nghiên cứu trong nước: chưa được nghiên cứu nhiều, các giải pháp đã nghiên cứu thì chưa phát hiện được nhiều vật thể[1] hoặc mức độ hỗ trợ còn hạn chế[2].
- Vậy trong đề tài này nhóm tiến hành nghiên cứu ra giải pháp thông minh hơn có ứng dụng học máy và thiết bị nhúng giúp
    - Hỗ trợ người khiếm thị tốt hơn trong việc đi lại trên đường phố đô thị.
    - Tăng tính chủ động trong việc đi lại


# Giải pháp
- Các chức năng của hệ thống
    - Chức năng chụp và lưu ảnh từ camera
    - Chức năng thông báo ra loa
    - Chức năng gửi tọa độ GPS từ thiết bị tới máy chủ.
    - Nhận diện vật thể trong ảnh: mô hình thuật toán YOLOv3 (tóm tắt)
    - Thông báo tọa độ GPS: Hiển thị tọa độ thời gian thực của người dùng trên website nhóm
- Trình bày chi tiết cách hoạt động các chức năng theo 2 phần:

## Về phần cứng và truyền thông
- Sơ đồ khối thể hiện cách mà thiết bị vxl thông báo tọa độ tới website + mô tả bằng lời
- Sơ đồ khối cách kết nối các linh kiện và quy trình xử lý của thiết bị vxl giúp nhận diện và thông báo ra loa + mô tả bằng lời

## Về phần mềm
- Sơ đồ nguyên lý của website nhận tọa độ của thiết bị vxl và hiển thị lên giao diện.
- Tóm tắt giải thuật về học máy sử dụng
    - Yolov3: kiến trúc


# Kết quả (ghi lại quá trình triển khai in general)

## Huấn luyện mô hình học máy
- Dữ liệu input
    - Where or/and how
    - What is it like: độ phân giải, số kênh màu
    - How much: total/train/test
- Công cụ và framework đã dùng 
- Tham số, thông tin chi tiết của mô hình học máy
- Kết quả huấn luyện: mAP chi tiết, training chart?, bar chart mAP for each class?...
- Đánh giá kết quả: so với chỉ tiêu có thỏa mãn hay không

## Chức năng nhận diện
- Cách build
- Dữ liệu input:
    - Where or/and how
    - What is it like: độ phân giải, số kênh màu
- Điều kiện thực nghiệm:
    - Tham số hàm API: IoU threshold, NMS threshold, (*there is 1 more threshold in the prediction code. Search it!*)
- Kết quả: 
    - FPS, độ ổn định
    - Dùng 1 metric nào đó để đánh giá
- Đánh giá kết quả nhận diện:

## Chức năng thông báo tọa độ GPS
- Cách build
- Điều kiện thực nghiệm
- Output kết quả
- Đánh giá kết quả

# Kết luận
- Đánh giá chung
- Hướng phát triển

# Tài liệu tham khảo: 
- Đưa vào mọi đường dẫn tới các cite trong bài báo cáo: trang tool, bài hướng dẫn, tham số đề xuất
[1] http://203.162.10.111/index.php/jstic/article/view/14/3
[2] http://cdit.ptit.edu.vn/wp-content/uploads/2019/04/14.-Bai-bao-Che-tao-thiet-bi-ho-tro-NKT-edited-9.3.pdf


*TODO*: 
    - Ask around if i can do like: for each functionality in functionalities, explain your solution in 2 parts: hardware part and software part.
    - Ask around if machine learning algorithm is put in hardware section or in software section. I think it should be in software section, but in hardware section we also need to say where, when and how did we manage to use that algorithm on our Pi.