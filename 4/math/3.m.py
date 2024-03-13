import  math
n = float(input('Input number of sides: '))
s = float(input('Input the length of a side: '))

area = (n * pow(s,2))/ 4 * math.tan(math.pi / n)
print(f"The area of the polygon is: {area}")
