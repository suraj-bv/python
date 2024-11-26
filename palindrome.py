s = input('Enter the string: ')
n = len(s)

is_palindrome = True

for i in range(n//2):
    if s[i] != s[n - i - 1]:
        is_palindrome = False

if is_palindrome:
    print('Given string is a palindrome')
else:
    print('Given string is not a palindrome')