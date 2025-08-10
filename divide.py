class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        res = dividend // divisor
        if (dividend % divisor != 0) and ((dividend < 0) != (divisor < 0)):
            res = res + 1
            
        return res