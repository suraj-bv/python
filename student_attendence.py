class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count += 1
                if count == 2:
                    return False
        
        if 'LLL' in s:
            return False

        return True