# This code is for calculating the number of distinct ways to climb a staircase with n steps
# leetcode problem number 70 

from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second
