nums = [3, 0, 1, 5, 6, 2]

n = len(nums)
total_sum = (n * (n + 1)) / 2

missing_number = total_sum - sum(nums)
print(f"The missing number is: {int(missing_number)}")

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        nums = set(nums)
        for i in range(1,n+1):
            if i not in nums:
                res.append(i)
        
        return res
