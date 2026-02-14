class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = len(s) - ones
        
        # Reserve one '1' for the last position
        return '1' * (ones - 1) + '0' * zeros + '1'