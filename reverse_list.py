# n = input('Enter the no. of items to insert: ')

# items = []

# for i in range(n):
#     item = input(f'Enter item {i+1}: ')
#     items.append(item)

# def reverse(items):
#     while(len(items) >-1):
#         items[]

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-1-i] = s[n-1-i], s[i]


sol = Solution()
sol.reverseString(["h", "e", "l", "l", "o"])
