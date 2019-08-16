import time
import calendar

print(time.time())  # Number of ticks since 12:00am, January 1, 1970


# Getting current time

localtime = time.localtime(time.time())

# This result, which could be formatted in any other presentable form
print(localtime)


# Getting formatted time

localtime = time.asctime(time.localtime(time.time()))

print(localtime)


# Getting calendar for a month

cal = calendar.month(2019, 1)

print(cal)
