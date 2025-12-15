class Solution:
    def toHex(self, num: int) -> str:
        # Special case: zero
        if num == 0:
            return "0"

        # If the number is negative, convert it to unsigned 32-bit
        if num < 0:
            num += 2**32

        hex_chars = "0123456789abcdef"
        result = []

        # Convert using repeated extraction of 4 bits at a time
        while num > 0:
            digit = num & 0xF             # remainder 0–15
            result.append(hex_chars[digit])
            num >>= 4                     # drop the last 4 bits

        # The digits are collected in reverse order
        return "".join(reversed(result))