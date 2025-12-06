class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ");
        res = [''] * len(words)
        for word in words:
            idx = int(word[-1])
            word = word[:len(word)-1]
            res[idx-1] = word
            


        return " ".join(res)