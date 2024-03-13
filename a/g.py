import re

list = []
txt = input()
camel = re.split('_', txt)
for i in camel:
    list.append(i.capitalize())
camel_case = "".join(list)
print(camel_case)