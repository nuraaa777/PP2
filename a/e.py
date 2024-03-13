import re

txt = input()
regex = re.search('a.(b{1})',txt)
if regex:
    print("True")
else:
    print("False")

