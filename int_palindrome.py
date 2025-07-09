num = int(input('Enter the number: '))
is_palindrome = False
original_num = num

# Function to reverse the digits of a number
# This function takes an integer as input and returns its reverse.
# If the input is an negative number it returns false as negative numbers are not considered palindromes.

def reverse(num):
    if num < 0:
        return 'Given number is not a palindrome'
    reversed_num = 0
    while(num != 0):
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

print(reverse(num))
print(f'Reverse of num = {reverse(num)}')

if original_num == reverse(original_num):
    print('Given number is a palindrome')
else:
    print('Given number is not a palindrome')