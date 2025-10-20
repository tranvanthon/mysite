def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

n = int(input("Moi nhap vao so: "))
# fibonaci_value = f(n)
for i in range(1, n+1, 1):
    fibonaci_value = f(i)
    print(fibonaci_value, end=" ") # end = " " để cho dãy số thành hàng ngang 
      