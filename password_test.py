password = input('Enter the password: ')

has_upper = has_lower = has_digit = has_splchar = False
splchar = ['!', '@', '#', '$', '^', '&', '*', '(', ')', '~', ':']

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char in splchar:
        has_splchar = True

if has_digit and has_lower and has_splchar and has_upper:
    print('STRONG')
elif (has_upper and has_lower and has_digit) or (has_digit and has_splchar and has_lower):
    print('MODERATE')
else:
    print('WEAK')