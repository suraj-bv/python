from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]

            if rightSum == leftSum:
                return i

            leftSum += nums[i]

        return -1
