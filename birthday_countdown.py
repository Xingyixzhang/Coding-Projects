import time
from datetime import date

today = date.today()
my_birthday = date(today.year, 6, 4)

if my_birthday < today:
    my_birthday = my_birthday.replace(year = today.year + 1)

days_to_birthday = abs(my_birthday - today)
print(days_to_birthday.days)