from typing import List
import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        
        nums.sort()
        return nums