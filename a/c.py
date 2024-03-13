import re

txt = input()
regex = re.search('[a-z]{1}(_){1}', txt)
if regex:
    print("True")
else:
    print("False")


