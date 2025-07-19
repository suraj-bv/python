class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate 

# majority element is the element that appears more than n/2 times in the array
# its only valid if there are only two types of elements in the array