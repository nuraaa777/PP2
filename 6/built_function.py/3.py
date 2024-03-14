import string
def Polindrome(txt):
    # string1 = string.lower().replace(' ','')
    string1 = ''.join(txt)
    first = 0
    last = len(txt)-1
    while first < last:
        if string1[first] ==string1[last]:
            first += 1
            last -= 1
        else:
            return  'String None Polindrome'
        return 'String Polindrome'
txt = input()
print(Polindrome(txt))
