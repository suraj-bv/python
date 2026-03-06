class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        
        # Move through the array until just before the last element
        while i < n - 1:
            if bits[i] == 0:
                i += 1      # one-bit char
            else:
                i += 2      # two-bit char
        
        # If we land exactly on the last index, it's a one-bit character
        return i == n - 1