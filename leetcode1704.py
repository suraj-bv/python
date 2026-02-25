class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        n = len(s) // 2
        count = 0

        for i in range(n):
            if s[i] in vowels:
                count += 1
            if s[i + n] in vowels:
                count -= 1

        return count == 0