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


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for c in s:
            if c.isalnum():
                cleaned += c.lower()

        for i in range(len(cleaned) // 2):
            if cleaned[i] != cleaned[len(cleaned) - i - 1]:
                return False

        return True
