class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for char in magazine:
            if char not in freq.keys():
                freq[char] = 1
            elif char in freq.keys():
                freq[char] += 1

        for char in ransomNote:
            if (char not in freq.keys()) or freq[char] < 1:
                return False
            elif char in freq.keys():
                freq[char] -= 1

        return True