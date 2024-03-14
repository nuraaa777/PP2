with open('aka.txt') as f:
    with open('b.txt', 'w') as f2:
        for i in f:
            f2.write(i)
f.close()
#Second way

import shutil
shutil.copy('aka.txt','b.txt')