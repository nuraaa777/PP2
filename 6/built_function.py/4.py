import time
import math

num = int(input('Input number: '))
millisecond = int(input('Input millesecond: '))
time.sleep(millisecond / 1000)

res = math.sqrt(num)
print(f'Square root of {num} after {millisecond} milliseconds is {res}')
