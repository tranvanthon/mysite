import time

# second = time.time()

# print(second)

# print(time.ctime(0)) # Trả về thời gian 08:00:00 01/01/1970 UTC
# print(time.ctime(second)) # Trả về thời gian Mon Oct 13 14:50:14 2025 UTC Hiện tại nó tương đương 
# print(time.ctime()) # Trả về thời gian Mon Oct 13 14:50:14 2025 UTC Hiện tại
# deplay = time.sleep(1) # Trả về thời gian Mon Oct 13 14:50:14 2025 UTC Hiện tại
# now = time.localtime()
# hour = now.tm_hour
# minute = now.tm_min
second = 0

# print(now.tm_hour)
# print(now.tm_min)
# print(second)
# # Tạo đồng hồ giây:
# while True:
#     print(second)
#     second += 1
#     time.sleep(1) 
# t = time.gmtime()
# cerrent = time.strftime("%d - %m - %Y %H:%M:%S", t)
# print(cerrent)

"""Cách tạo đồng hồ"""
from datetime import datetime


while True:
    now = datetime.now()
    current_time = now.strftime("%H : %M : %S")
    if now.minute > float(current_time("%S")):
        print(current_time)
        time.sleep(1)
    else:
        print(current_time)





