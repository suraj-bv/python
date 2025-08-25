from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]

        n = len(nums)
        totalSum = (n * (n + 1)) // 2
        missing = totalSum - currSum + res[-1]

        res.append(missing)

        return res