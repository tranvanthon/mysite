# Viết chương trình nhập vào từ bàn phím bán kính r của đường
# tròn, in ra kết quả (cho pi = 3.14)
# a. Chu vi = ? 2*r*3.14
# Dien  tich = ? 3.14*(r**2)
import math


r = float(input("Nhập bán kính đường tròn:"))
pi = math.pi

perimerter = 2*pi*r
area = pi*(r**2)

print("Chu vi va dien tich lan luot la", perimerter, area)
print(f"Chu vi la {perimerter} va dien tich la {area}")
print("Chu vi la {}, dien tich la {}" .format(perimerter, area))



