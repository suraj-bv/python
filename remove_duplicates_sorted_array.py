class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    break
                else:
                    total += 1

        return total