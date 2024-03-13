import re

from datetime import date, timedelta

today = date.today()
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)

print(tomorrow)
print(today)
print(yesterday)
