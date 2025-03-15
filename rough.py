from datetime import datetime

today = datetime.today()

print(today.year, today.month,today.day)
print(today.strftime("%Y%m%d"))
date = int(today.strftime("%Y%m%d"))
print(date+1)


b_ = 45729
that_day = 20250313
bl=date-that_day

b = b_ + bl
print(b)