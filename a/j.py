txt = str(input())
result = re.findall('[A-Z][a-z]*', txt)
for i in result:
    x = i.lower()
    print(x, end="_")
