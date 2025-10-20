# """
# Viet chuong trinh chuyen tin nhan sang mat ma theo bang:
#     a = "abcdefghijklmnopqrstuvwxyz"
#     b= "zxcvbnmasdfghjklqwertyuiop"
# """

# a = "abcdefghijklmnopqrstuvwxyz"
# b = "z?><%~]asd#@$jkl&*^tyuiop"

# n = input("Moi nhap vao noi dung thu: ")
# for i in n:
#     index = a.find(i)
#     print(b[index], end="")


#
#     For string:
#     a = """
#           toi cham hoc toi chiu kho toi dep trai
# """
a = """
    toi cham hoc
    toi chiu kho
    toi dep trai toi toi
"""
count_a = 0
# print(b)

for i in range(len(a)):
    if a[i] == "t" and a[i + 1] == "o" and a[i + 2] == "i":
        count_a += 1
        print(count_a)
