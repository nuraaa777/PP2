import string
string = input()
l_lower = []
l_upper = []
count1 = 0
count2 = 0
for i in string:
    if 'A' <= i <= 'Z':
        l_upper.append(i)
        count1 +=1
    elif 'a' <= i <= 'z':
        l_lower.append(i)
        count2 +=1

print(f'Upper Case: {count1}')
print(f'Lower Case: {count2}')

# Built Function

txt = input()
upper = 0
lower = 0
for i in txt:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1

print(f'Upper case: {upper}')
print(f'Lower case: {lower}')
