import os

path = input()

path2 = os.getcwd()

print(os.path.exists(path))

print(os.path.exists(path2))

os.remove(path)

os.remove(path2)