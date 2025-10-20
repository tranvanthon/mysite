import random
list_class = [
    "Phan Hoàng Anh", "Trương Thị Như Bình", "Lâm Thanh Duy", "Nguyễn Tiến Đạt", "Nguyễn Hải Đăng",
    "Nguyễn Thị Mỹ Hạnh","Lê Mai Chí Hiền","Cao Văn Lê Hoài","Nguyễn Khải Hoàng","Lê Thị Thanh Hương",
    "Tạ Minh Kha","Phạm Đăng Khoa","Lư Phan Đăng Khoa","Trương Tấn Khoa","Võ Thị Ngọc Lam",
    "Nguyễn Trần Phi Long","Lê Nguyễn Huỳnh Mai","Nguyễn Huỳnh Diễm My","Huỳnh Lê Ngọc Ngân","Liêu Khôi Nguyên",
    "Phan Trần Vạn Nguyên","Nguyễn Thanh Nhật","Phan Ngọc Bình Nhi","Huỳnh Thị Ngọc Như","Dương Thanh Phú",
    "Hồ Thị Đào Quyên","Nguyễn Thành Tài","Trần Văn Tấn","Nguyễn Hoàng Thịnh","Nguyễn Trương Minh Thùy",
    "Võ Ngọc Tuyền","Nguyễn Thị Thanh Thúy","Nguyễn Derik Thành Trí","Ngô Thanh Trí","Nguyễn Lam Trường",
    "Lư Nguyễn Ngọc Vy","Lê Văn Bảo Vinh","Nguyễn Lê Thanh Vân","Nguyễn Thị Đào Uyên","Nguyễn Thị Minh Tuyết",
    "Dương Thị Như Ý",
    ]

"""while True:
    try:
        user = int(input("Nhập số thứ tự (1 - 41, 0 để thoát):"))
        if user == 0:
            print("Tạm biệt 👋")
            break
        elif 1 <= user <= len(list_class):
            print(f"Số {user} là: {list_class[user - 1]}") 
        else:
            print("❌ Số không hợp lệ! Vui lòng nhập từ 1 đến 41.")

    except ValueError:
        print("⚠️ Vui lòng nhập số hợp lệ!")"""

for i in random.choice(list_class):
    user = input("Nhấn Enter để chọn người ngẫu nhiên (hoặc nhập 'q' để thoát): ")
    if user == "":
        rander_user = random.choice(list_class)
        print(rander_user)
    elif user.lower() == "q":  # cho phép thoát
        print("Kết thúc chương trình.")
        break
    else:
        print("❌ Bạn đã nhập ký tự khác, vui lòng nhấn Enter hoặc 'q'.")
