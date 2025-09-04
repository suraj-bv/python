from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
        
        res = []
        for word in words:
            letters = set(word)
            if letters.issubset(row1) or letters.issubset(row2) or letters.issubset(row3):
                res.append(word)
        return res