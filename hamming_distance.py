class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR gives 1s only at differing bit positions
        xor_result = x ^ y
        
        # Count the number of 1s (set bits) in xor_result
        # In Python 3.8+, bit_count() gives the popcount
        return xor_result.bit_count()