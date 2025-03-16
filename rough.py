from datetime import datetime

today = datetime.today()

# # print(today.year, today.month,today.day)
# today.strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))
# date = int(today.strftime("%Y%m%d"))
# # print(date+1)


# bb = 45729
# that_day = 20250313
# bl=date-that_day

# b = bb + bl
# print(b)
date = str(today.strftime("%Y%m%d"))
print(type(date))