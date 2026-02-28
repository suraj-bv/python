from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        return max_val*k+(k*(k-1))//2