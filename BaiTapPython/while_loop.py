# # while được sử dụng khi không biết số lần lặp lại là bao nhiêu
# n = int(input("Please enter a number:"))

# while n <= 0 or n > 99:
#     n = int(input("The value you entered is not a number. Please try again!"))

# print("The number you entered is: {}" .format(n))
"""# Excercise1: use while -else, break:
# Chương trình tuyển học sinh giỏi:
# # Yêu cầu:
# 1. Nhập vào học tên học sinh.
# 2. Môn dự thi.
# 3. Điểm thi
# In ra màn hình học sinh được chọn, nếu: môn dự thi từ 7 trở lên.
# Khi user nhan N is exit"""

# Nhập học tên:


while True:
    full_name = input("Please enter username:")
    subject = input("Please enter Exam subjects:")
    test_cores = float(input("Please enter test cores:"))
    if test_cores > 7:
        print(f"Students {full_name} are eligible to take the exam")
    else:
        print(f"Students {full_name} aren'/t eligible to take the exam")
    
    is_exit = input("Press n to exit or press any key to continue!:")
    if is_exit == "n" or is_exit == "N":
        break



