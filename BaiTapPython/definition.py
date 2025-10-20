# # Define with agrument
# def addition(x,y):
#     return x + y

# def subtraction(x,y):
#     return x - y

# x = float(input("Please enter x value:"))
# y = float(input("Please enter y value:"))

# print(addition(x, y))
# print(subtraction(x, y))

# define without agrument
# def text_string(string):
#     return string

# export_string = input("Please enter yourstring: ")

# value_string = text_string(export_string)


# print(type(value_string))
# Sử dụng hàm def viết hàm tính tỉ lệ Roi = (doanh_thu-chi_phi)/chi_phi, nếu Roi>=0.75 print("Nên đầu tư"
def roi(doanh_thu, chi_phi):
    return (doanh_thu - chi_phi) / chi_phi


def dautu(roi):

    if roi >= 0.75:
        return "Nen dau tu"
    else:
        return "Khong dau tu"


doanh_thu = float(input("Doanh thu cua ban la: "))
chi_phi = float(input("Chi phi cua ban la: "))
dautu_value = roi(doanh_thu, chi_phi)

result = dautu(dautu_value)
# print(dautu_value)
# print(result)


def max_number(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_number = num
    return max_number


print(max_number(3, 7, 2, 9, 1))
