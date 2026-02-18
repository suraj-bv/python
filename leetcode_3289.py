from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        # Count frequencies
        freq = Counter(nums)

        # Return those with count == 2
        return [num for num, count in freq.items() if count == 2]