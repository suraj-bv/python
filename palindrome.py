s = input('Enter the string: ')
n = len(s)
is_palindrome = True

for i in range(n // 2):  # Loop through the first half of the string
    if s[i] != s[n - i - 1]:  # Compare with the corresponding character from the end
        is_palindrome = False
        break

if is_palindrome:
    print('String is a palindrome')
else:
    print('String is not aSURA palindrome')
