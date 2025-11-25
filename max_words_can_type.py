class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        words = text.split(" ")
        for word in words:
            can_type = True
            for char in word:
                if char in brokenLetters:
                    can_type = False
            if can_type:
                count += 1

        return count