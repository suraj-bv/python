class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        
        # Step 1: Skip whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Check overflow
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            num = num * 10 + digit
            i += 1
        
        return sign * num