path = input()

with open(path, 'r') as re:
    x = len(re.readlines())
    print('Total lines:', x)