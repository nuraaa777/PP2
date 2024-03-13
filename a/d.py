import re

txt = input()
regex = re.search('^[A-Z]{1}([a-z]*)$',txt)
if regex:
    print("True")
else:
    print("False")

