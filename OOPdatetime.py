import datetime
from datetime import date

Tony_birthday = datetime.datetime(1996, 5, 6)

Today_date = datetime.datetime.now()


# 8546 days has passed since my birth
print(Today_date - Tony_birthday)

# print(dir(datetime))

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

Today = date.fromtimestamp(1234567890)
print(Today)
print(datetime.datetime.now())