from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1, -1]

        idx = []
        for i in range(len(nums)):
            if nums[i] == target:
                idx.append(i)

        return idx[0], idx[-1]