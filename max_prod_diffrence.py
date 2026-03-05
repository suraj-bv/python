class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        max_prod = nums[-1] * nums[-2]
        min_prod = nums[0] *nums[1]

        return max_prod-min_prod