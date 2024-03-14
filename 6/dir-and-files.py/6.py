import string

for i in string.ascii_uppercase:
    with open(f'{i}.txt', 'w') as file:
        file.write(f'{i}')

file.close()