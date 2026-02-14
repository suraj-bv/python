class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        
        # Build next greater mapping for nums2
        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        
        # For remaining elements not popped, no greater element
        for rem in stack:
            next_greater[rem] = -1
        
        # Construct result for nums1
        return [next_greater[x] for x in nums1]