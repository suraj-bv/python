class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(65 <= ord(ch) <= 90 for ch in word):
            return True

        if all(97 <= ord(ch) <= 122 for ch in word):
            return True

        if 65 <= ord(word[0]) <= 90 and all(97 <= ord(ch) <= 122 for ch in word[1:]):
            return True
            
        return False