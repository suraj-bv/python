original_num = int(input('Enter the number: '))

def reversed(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

print(f'Reverse of num = {reversed(original_num)}')

if original_num == reversed(original_num):
    print('Given number is a palindrome')
else:
    print('Given number is not a palindrome')