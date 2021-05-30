# Giới thiệu
*TODO*

# Giải pháp
- Các chức năng của hệ thống
    - Nhận diện: Thiết bị vi xử lý liên tục chụp và nhận diện các vật cản hoặc người thân trong bức ảnh sau đó phát âm thanh (giọng nói) ra loa nếu phát hiện bất kỳ vật cản hay người thân trong bức ảnh đã chụp.
    - Thông báo tọa độ GPS: Hiển thị tọa độ thời gian thực của người dùng trên website nhóm
- Trình bày chi tiết cách hoạt động các chức năng theo 2 phần:

## Về phần cứng và truyền thông
- Sơ đồ khối thể hiện cách mà thiết bị vxl thông báo tọa độ tới website + mô tả bằng lời
- Sơ đồ khối cách kết nối các linh kiện để nhận diện và thông báo ra loa + mô tả bằng lời
- Sơ đồ khối quy trình xử lý của thiết bị vxl giúp nhận diện và thông báo ra loa + mô tả bằng lời

## Về phần mềm
- Sơ đồ nguyên lý của website nhận tọa độ của thiết bị vxl và hiển thị lên giao diện.

*TODO*: 
    - Ask around if i can do like: for each functionality in functionalities, explain your solution in 2 parts: hardware part and software part.
    - Ask around if machine learning algorithm is put in hardware section or in software section. I think it should be in software section, but in hardware section we also need to say where, when and how did we manage to use that algorithm on our Pi.

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
