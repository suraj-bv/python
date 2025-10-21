class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {}
        consonants = {}

        for char in s:
            if char in 'aeiou':
                if char in vowels:
                    vowels[char] += 1
                elif char not in vowels:
                    vowels[char] = 1
            else:
                if char not in consonants:
                    consonants[char] = 1
                elif char in consonants:
                    consonants[char] += 1
        
        max_vowel = max(vowels.values()) if vowels else 0
        max_conso = max(consonants.values()) if consonants else 0

        return max_vowel + max_conso