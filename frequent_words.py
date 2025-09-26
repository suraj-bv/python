from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        
        banned_set = set(banned)
        freq = {}
        
        for word in words:
            if word not in banned_set:
                freq[word] = freq.get(word, 0) + 1
        
        max_word = ""
        max_count = 0
        for word, count in freq.items():
            if count > max_count:
                max_count = count
                max_word = word
        
        return max_word