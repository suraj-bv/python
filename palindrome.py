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


from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        odd_found = False

        for count in freq.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                odd_found = True

        if odd_found:
            length += 1

        return length


from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            n = len(word)
            is_palindrome = True
            for i in range(n):
                if word[i] != word[n - i -1]:
                    is_palindrome = False
            
            if is_palindrome:
                return word

        return ''