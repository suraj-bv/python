from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = []
        for word in words:
            add = True
            for i in range(len(word)):
                if word[i] not in chars:
                    add = False
            if add:
                res.append(word)
        
        result = 0
        for word in res:
            result += len(word)

        return result

from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= char_count[c] for c in word_count):
                total_length += len(word)

        return total_length