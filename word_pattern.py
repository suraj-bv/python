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




class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()

        for ch1, ch2 in zip(s, t):
            if ch1 not in mapping:
                if ch2 in used:
                    return False
                mapping[ch1] = ch2
                used.add(ch2)
            else:
                if mapping[ch1] != ch2:
                    return False

        return True