class Solution:
    def nonRepeatingChar(self,s):
        count = [0] * 26
        
        for c in s:
            count[ord(c) - 97] += 1
            
        for c in s:
            if count[ord(c) - 97] == 1:
                return c
        
        return '$'