class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        chars = s.split()
        nums = []
        for char in chars:
            if char.isdigit():
                nums.append(char)
        
        is_ascending = True

        for i in range(len(nums)-1):
            if int(nums[i]) >= int(nums[i+1]): 
                is_ascending = False

        return is_ascending