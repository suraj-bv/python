from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sumSingle = 0
        sumDouble = 0

        for num in nums:
            if num % 10 == num: 
                sumSingle += num
            else:
                sumDouble += num

        return not(sumSingle == sumDouble)