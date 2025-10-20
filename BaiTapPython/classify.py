"""Viết chương trinh nhập vào điểm trung bình môn, cho biết điểm đó thuộc loại: khá, giỏi, tb, yếu nếu:
    >= 9 loại giỏi,
    7.0 <= average < 9.0: Khá
    5.0 <= average < 7.0 : TB
    < 5.0 : Yếu
"""
average = float(input("Please enter the number average:"))

if average >= 0 and average <= 10:
    if average >= 9:
        print(f"Your {round(average), 2} is Excellent.")

    elif average >= 7:
        print(f"Your {round(average), 2} is Petty good.")

    elif average >= 5:
        print(f"Your {round(average), 2} is Average.")

    else:
        print(f"Your {round(average), 2} is Weak.")
else:
    print(f"The value must be a number in 0 to 10")
    average = float(input("Please enter the number average:"))