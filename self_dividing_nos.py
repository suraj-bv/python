from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            num = i
            add = True
            while num > 0:
                digit = num % 10
                if digit == 0 or i % digit != 0:
                    add = False
                    break
                num //= 10
            if add:
                res.append(i)
        
        return res