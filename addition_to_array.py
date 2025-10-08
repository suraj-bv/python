from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = k
        res = []

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
            res.append(carry % 10)
            carry //= 10
            i -= 1

        return res[::-1]