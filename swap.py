def swap_by_arithmetic_op(a, b):
    a = a - b
    b = a + b
    a = a - b
    return a, b

a, b = 20, 30
print(f'Before swapping using arithmetic operations: a = {a}, b = {b}')
a, b = swap_by_arithmetic_op(a, b)
print(f'After swapping using arithmetic operations: a = {a}, b = {b}')

def swap_by_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

a, b = 20, 30
print(f'Before swapping using XOR: a = {a}, b = {b}')
a, b = swap_by_xor(a, b)
print(f'After swapping using XOR: a = {a}, b = {b}')

def swap_by_py(a, b):
    a, b = b, a
    return a, b

a, b = 20, 30
print(f'Before swapping using Python: a = {a}, b = {b}')
a, b = swap_by_py(a, b)
print(f'After swapping using Python: a = {a}, b = {b}')
