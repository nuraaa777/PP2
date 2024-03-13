import re

txt = input()
result = re.findall('[A-Z][a-z]*', txt)
for i in result:
    print(i, end = " ")