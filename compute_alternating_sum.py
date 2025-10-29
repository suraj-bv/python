from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        add_sum = 0
        sub_sum = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                add_sum += nums[i]
            else:
                sub_sum += nums[i]
        
        return add_sum - sub_sum