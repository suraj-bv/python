from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        if sortedNums[-1] >= sortedNums[-2] * 2:
            return nums.index(sortedNums[-1])

        return -1
