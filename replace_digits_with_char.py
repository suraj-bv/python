class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if i % 2 == 1:
                if s[i].isdigit() == True:
                    add = int(s[i])
                prev = ord(s[i-1])
                new_char = chr(prev+add)
                s[i] = new_char

        return ''.join(s)