class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        nums = list(num)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != '0':
                break
            elif nums[i] == '0':
                nums.pop()

        return ''.join(nums)
