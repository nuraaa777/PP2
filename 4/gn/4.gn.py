def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2

# Testing the generator with a for loop
a = 1
b = 5

print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)
