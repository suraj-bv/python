from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res = []
        while len(nums) > 1:
            numsMin = min(nums)
            numsMax = max(nums)
            nums.remove(numsMin)
            nums.remove(numsMax)

            minMaxAvg = (numsMin + numsMax) / 2
            res.append(minMaxAvg)


        return min(res)