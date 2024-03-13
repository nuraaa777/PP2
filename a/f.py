import re

txt = input()
regex = re.sub('[ ,.]', ":",txt)
print(regex)
