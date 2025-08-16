class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1
    
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        
        for i in range(len(num) - 2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:
                if sub > max_good:
                    max_good = sub
                    
        return max_good


class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = list(str(num))
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break
        return int("".join(num_str))

