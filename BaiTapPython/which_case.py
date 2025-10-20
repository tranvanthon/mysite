# while True:
#     day_input = input(
#         """
#         Thứ CN: bấm số 0
#         Thứ 2: bấm số 1
#         Thứ 3: bấm số 2
#         Thứ 4: bấm số 3
#         Thứ 5: bấm số 4
#         Thứ 6: bấm số 5
#         Thứ 7: bấm số 6
#     """
#     )
#     if not day_input.isdigit():
#         print("❌ Vui lòng chỉ nhập số từ 0 đến 6!")
#         continue

#     day = int(day_input)

#     # if 0 <= day_input <= 6:
#     match day_input:
#         case 0:
#             print("Chủ nhật")

#         case 1:
#             print("Thu hai")

#         case 2:
#             print("Thu ba")

#         case 3:
#             print("Thu tu")

#         case 4:
#             print("Thu nam")

#         case 5:
#             print("Thu Sau")

#         case 6:
#             print("Thu Bay")
#         case _:
#             print(
#                 "Không có  các thứ này nghe!"
#             )  # Nếu không có số nào hợp thì nó sẽ chạy case _:

while True:
    day_input = int(input("Nhap vao mot so: "))

    match day_input:
        case 1 | 2 | 3 | 4 | 5:
            print("Today is weekend!")
        case 6 | 7:
            print("Tody love weekend!")
        case _:
            print("What happen!")
