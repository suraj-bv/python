from typing import List

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

class Solution:
    def findMajority(self, arr):
        if not arr:
            return []
        
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None
        
        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        
        for c in [candidate1, candidate2]:
            if arr.count(c) > len(arr) // 3 and c not in result:
                result.append(c)
                
        return sorted(result)
    
# This code calculates the majority elements in an array
# It finds elements that appear more than n/3 times, where n is the length of the array
# leetcode problem number 229