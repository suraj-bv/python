def swap(a, b):
    a = a - b
    b = a + b
    a = a - b
    return a, b

a, b = 20, 30
print(f'Before swapping: a = {a}, b = {b}')
a, b = swap(a, b)
print(f'After swapping: a = {a}, b = {b}')