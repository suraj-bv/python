class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ''
        for i in range(len(word)):
            if word[i] == ch:
                prefix = word[:i+1]
                word = word[i+1:len(word)]
                break

        rev_prefix = prefix[::-1]
        return rev_prefix + word