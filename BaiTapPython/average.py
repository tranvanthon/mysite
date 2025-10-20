# Viết chương trình:
#     1. Nhập vào từ bàn phím thời gian về đích của vận động viên (tính bằng s)?
#     2. Xuất ra màn hình thời gian về đích average = sum(athlete1, athlete2, athlete3)/3

athlete1 = float(input("Thoi gian ve dich cua van dong vien 1:"))
athlete2 = float(input("Thoi gian ve dich cua van dong vien 2:"))
athlete3 = float(input("Thoi gian ve dich cua van dong vien 3:"))

# Thời gian về đích của từng vận động:
print(f" Thời gian về đích của VDV1 {athlete1} s,  Thời gian về đích của VDV3 {athlete2} s, Thời gian về đích của VDV3 {athlete3} s") 
# Thời gian trung bình của 3 athlete:
average = sum([athlete3, athlete2, athlete1],0)/3

print(f"Trung binh thoi gian ve dich cua vdv la: {average}")

