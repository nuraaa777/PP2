path = os.getcwd()
print('Directors: ')
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
print('\nFiles: ')
for j in os.listdir(path):
    if os.path.isfile(os.path.join(path, j)):
        print(j)
print('\nAll Directors and Files: ')

for index, folder,file in os.walk(path):
    for i in folder:
        print(os.path.join(index, i))
    for j in file:
        print(os.path.join(index, j))
