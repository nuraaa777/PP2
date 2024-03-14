from functools import reduce

def func(txt):
    return reduce(lambda x,y: (x+y)**2,txt)


txt = [1,2,3]
print(func(txt))