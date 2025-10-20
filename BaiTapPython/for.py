# while True:
#     a = int(input("Moi nhap so nguyen:"))
#     if a % 2 == 0:
#         for i in range(1, 6, 1):
#             a += i
#         print(a)
#     else:
#         print("Xin loi chung toi 0 tinh tong le! Byebye")
    


# # Tạo bản cửu chương
# for i in range(10):
#     for j in range(10):
#         print(f"{i} * {j} = {i*j}")
#     print(f"#"*10 )

"""#Tao chu N
n = int(input("Moi nhap chieu cao cua ky tu can tao:"))

for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == j:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()"""

    #Tao chu c>

for i in range(7):
    for j in range(7):
        if (i == 0 and j in (1, 2, 4, 5)) or (i == 1 and j in (0, 3, 6)) or (i == 2 and j in (0, 6)) or (i == 3 and j in (1, 5)) or (i == 4 and j in (2, 4)) or (i == 5 and j == 3):
            print(f"💚", end=" ")
        else:
            print(" ", end=" ")
    print()