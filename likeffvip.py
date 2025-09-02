import requests
import json
import threading

# Hàm thực hiện yêu cầu API cho mỗi ID
def like_tool(api_url, key, uid, region):
    # Thiết lập các tham số cần thiết
    params = {
        "key": key,
        "uid": uid,
        "region": region
    }

    try:
        # Gửi yêu cầu GET đến API
        response = requests.get(api_url, params=params)

        # Kiểm tra mã trạng thái HTTP của phản hồi
        if response.status_code == 200:
            # Lấy dữ liệu JSON từ phản hồi
            data = response.json()

            # Kiểm tra trạng thái thành công
            if data.get("status") == 1:
                print(f"ID {uid} - Gọi API thành công!")
                print(f"Nickname của người chơi: {data['PlayerNickname']}")
                print(f"Likes trước khi thực hiện lệnh: {data['LikesbeforeCommand']}")
                print(f"Likes sau khi thực hiện lệnh: {data['LikesafterCommand']}")
                print(f"Cấp độ người chơi: {data['Level']}")
                print(f"Khu vực: {data['Region']}")
                print(f"UID người chơi: {data['UID']}")
            else:
                print(f"ID {uid} - API trả về lỗi: Không thể tăng likes.")
        else:
            print(f"ID {uid} - Lỗi khi gọi API. Mã lỗi HTTP: {response.status_code}")

    except Exception as e:
        print(f"ID {uid} - Đã xảy ra lỗi: {e}")

# Hàm để gọi nhiều luồng xử lý các ID
def handle_multiple_ids(api_url, key, region, uid_list):
    threads = []

    # Duyệt qua danh sách UID và tạo các luồng
    for uid in uid_list:
        thread = threading.Thread(target=like_tool, args=(api_url, key, uid, region))
        threads.append(thread)
        thread.start()  # Bắt đầu luồng mới

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

# Chạy công cụ với nhiều ID
if __name__ == "__main__":
    # URL của API
    api_url = "http://103.149.253.241:2010/like"
    
    # Các tham số cần thiết
    key = "conbo"  # Khoá API
    region = "sg"  # Khu vực người chơi

    # Hiển thị thông báo đáng yêu
    print("Nhập ID Game Phờ Ri Phai Của Mày Vào Đây Cho Bot Cute Này Tăng Like Cho Hiểu Chưa Đồ Đáng Iu Kia")
    
    # Nhập các UID từ bàn phím
    uid_list_input = input("Nhập danh sách UID, cách nhau bằng dấu phẩy: ")
    
    # Chuyển chuỗi nhập vào thành danh sách các UID
    uid_list = [int(uid.strip()) for uid in uid_list_input.split(',')]

    # Gọi hàm xử lý với danh sách UID
    handle_multiple_ids(api_url, key, region, uid_list)
