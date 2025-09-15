class Solution:
    def areRotations(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        i = 0
        while i < len(s1):
            if s1 == s2:
                return True
                
            s1 = s1[1:] + s1[0]
            
        return False
    
# The time complexity of this function is O(n^2) in the worst case,
# where n is the length of the strings. This is because for each character in s1
# we are checking all characters in s2.

class Solution:
    def areRotations(self, s1, s2):
        return len(s1) == len(s2) and s2 in (s1 + s1)
    
# The time complexity of this optimized function is O(n),
# where n is the length of the strings. This is because we are concatenating s1


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False