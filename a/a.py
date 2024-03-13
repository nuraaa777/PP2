import re
txt = input()
regex = re.search('^a(b*)$', txt)
if regex:
    print("True")
else:
    print("False")


