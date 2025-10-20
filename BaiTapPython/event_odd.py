# Viết chương trình nhập vào số nguyên từ bàn phím, xuất kết quả chẵn hay lẻ
number = int(input("Please enter the number:"))


if number%2 == 0:
    print(f"Number {number} is odd")
else:
    print(f"So {number} is event")

# a =""" #Dùng để chú thích cũng có thể xuất ra nhiều dòng văn bản.
#     (venv) thontv@thontv-M5-PLUS:~/mysite$ /home/thontv/venv/bin/python /home/thontv/mysite/BaiTapPython/average.py
# Thoi gian ve dich cua van dong vien 1:54
# Thoi gian ve dich cua van dong vien 2:54
# Thoi gian ve dich cua van dong vien 3:57
#  Thời gian về đích của VDV1 54.0 s,  Thời gian về đích của VDV3 54.0 s, Thời gian về đích của VDV3 57.0 s
# """
# print(a)