list1 = ['Rozimurad', 'Mango', 'Banana', 'Samandar','KBTU']
path = 'b.txt'
with open(path, 'w') as wr:
    wr.writelines(f'{list1}\t')
wr.close()