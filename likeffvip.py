import requests

def get_like_data(api_url, key, uid, region):
    # Tạo URL yêu cầu
    url = f"{api_url}/like?key={key}&uid={uid}&region={region}"
    
    try:
        # Gửi yêu cầu GET đến API
        response = requests.get(url)
        
        # Kiểm tra xem yêu cầu có thành công không
        if response.status_code == 200:
            # Chuyển dữ liệu trả về từ JSON thành dictionary
            data = response.json()
            
            # Trả về dữ liệu cần thiết
            return {
                "Likes Given By API": data.get("LikesGivenByAPI"),
                "Likes After Command": data.get("LikesafterCommand"),
                "Likes Before Command": data.get("LikesbeforeCommand"),
                "Player Nickname": data.get("PlayerNickname"),
                "Level": data.get("Level"),
                "Region": data.get("Region"),
                "UID": data.get("UID"),
                "Status": data.get("status")
            }
        else:
            print(f"Lỗi: {response.status_code}")
            return None
    except Exception as e:
        print(f"Lỗi: {e}")
        return None

def main():
    print("Chào mừng đến với Bot Tăng Like Cute!")
    print("Nhập ID Game Phờ Ri Phai Của Mày Vào Đây Cho Bot Cute Này Tăng Like Cho Hiểu Chưa Đồ Đáng Iu Kia")
    
    # Nhập ID game và các thông tin cần thiết
    uid = input("Nhập ID game của bạn: ")
    region = input("Nhập khu vực của bạn (ví dụ: sg, vn): ").strip().lower()

    # Cấu hình các tham số API
    api_url = "http://103.149.253.241:2010"
    key = "conbo"

    try:
        # Gọi hàm và lấy kết quả
        result = get_like_data(api_url, key, int(uid), region)
        
        # Hiển thị kết quả nếu có
        if result:
            print("\nThông tin từ API:")
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print("Không nhận được dữ liệu từ API. Vui lòng thử lại.")
    except ValueError:
        print("ID game phải là một số hợp lệ. Vui lòng nhập lại.")
    
if __name__ == "__main__":
    main()
