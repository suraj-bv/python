from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0
        for idx in range(len(nums)):
            if idx > maxIdx:
                return False
            elif maxIdx < nums[idx] + idx:
                maxIdx = nums[idx] + idx

        return True