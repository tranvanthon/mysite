"""
Viết chương trình cho phép người dùng nhập vào 1 chuỗi
    a. Hiển thị chuỗi ra màn hình
    b. Hiển thị ký tự đầu tiên và cuối cùng của chuỗi.
    c. Hiển thị các ký tự có vị trí index lẻ
"""

"""def string_text():
    n = input("Moi nhap vao chuoi bat ki")
    return n


# show string
def show(n):
    return n


def show_start_end(n):
    return n[0:-1]


enter_string = string_text()
start_end = string_text()
print(enter_string)
print(start_end)
"""
"""# Cac hàm xử lý:
str = "33333333333333Chao em33333333333333333333"
print(str)
a = str.strip("3")
print(len(str))
print(len(a))
print(a)
"""
# str = "tran van thon 3333333 Chao em 33333333333333333333"
# a = str.find("thon", 0, -1)
# print(a)
# b = str.capitalize()
# print(b)

# a = "dienvien1;Jackychan;01/11/1970"
# arr = a.split("Jacky")
# print(type(a))

# print(arr)

###### Bai 25.5
# Bai tap string 1: Cho str1 = "English = 78 Science = 83 Math = 69 History = 70"
# Tinh tong cac so trong string
"""str1 = "English = 78 Science = 83 Math = 69 History = 70"

str_value = str1.split()
total = 0
count = 0
for i in str_value:
    if i.isdigit():
        total = total + int(i)
        count += 1

print(f"Total of str1 is: {total}")
print(f"Average of str1 is: {total/count}")
"""
"""
Viet chuong trinh kiem tra tinh hop le cua mat khau:
* Mat khau co it nhat 6 ki tu chua it nhat 1 chu cai (Chu cai thuong hoac Hoa deu duoc)
* Chua it nhat 1 chu so
2. Cho nguoi dung nhap vao mat khau de login/ so sanh, neu dung mo cua, sai 5 lan 
khoa dang nhap va thoat chuong trinh
"""
special_chars = "!@#$%^&*()_+-=[]}{|;:'\",.<>?/"
while True:
    password = input("Moi nhap mat khau: ")

    has_upper = any(i.isupper() for i in password)
    has_special = any(i in special_chars for i in password)
    has_digit = any(c.isdigit() for c in password)
    has_alpha = any(c.isalpha() for c in password)

    lenght_ok = len(password) > 6

    if has_alpha and has_digit and lenght_ok and has_special and has_upper:
        print("Mat khau du dk")
        break
    else:
        print(
            "Mat khau phai tu 6 ki tu tro len va chua it nhat 1 so hoac 1 ki tu viet hoa va 1 ky tu dac biet !@#$%^&*()_+-=[]}{|;:'\",.<>?/"
        )


# login for user
count = 0
password1 = input("Moi nhap mat khau dang nhap: ")
while password != password1:
    count += 1
    print(f"Ban con thuc hien duoc {5 - count} lan")
    password1 = input("Nhap lai mat khau: ")
    if count == 4:
        print("Ban da sai mat khau qua 5 lan. Tai khoan ban bi khoa")
        break
else:
    print(f"Dang nhap thanh cong")
