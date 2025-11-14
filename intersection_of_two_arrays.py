class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)

        set2 = set(nums2)

# Intersection of the sets

        result_set = set1 & set2

        return list(result_set)