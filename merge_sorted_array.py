class Solution:
    def merge(self, nums1, m, nums2, n):
        # Set pointers to the end of the elements in nums1 and nums2
        i = m - 1  # last element of nums1's real content
        j = n - 1  # last element of nums2
        k = m + n - 1  # last position of nums1's total length

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left (nums1 is already there)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


class Solution:
    def kthElement(self, a, b, k):
        # code here
        new_list = a + b
        new_list.sort()
        
        return new_list[k-1]


from typing import List
# This code is for finding the median of two sorted arrays
# In this code we are merging the two arrays and then finding the median using + and / operators

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = nums1 + nums2
        newList.sort()
        res = len(newList) % 2
        if res == 0:
            mid = len(newList) // 2
            return (newList[mid - 1] + newList[mid]) / 2
        elif res == 1:
            mid = len(newList) // 2
            return newList[mid]