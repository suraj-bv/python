class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        mapping = {}
        used = set()
        
        for ch, word in zip(pattern, words):
            if ch not in mapping:
                if word in used:
                    return False
                mapping[ch] = word
                used.add(word)
            else:
                if mapping[ch] != word:
                    return False
        
        return True