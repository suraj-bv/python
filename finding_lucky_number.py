from typing import List
from collections import Counter

# Lucky number is defined as a number that has a frequency in the array equal to its value.
# Given an array of integers arr, return the largest lucky integer in the array. If there is no lucky integer return -1.

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        res = -1
        for num, count in freq.items():
            if num == count:
                res = max(res, num)
        return res