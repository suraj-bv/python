class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for sentence in sentences:
           words = sentence.split()
           if maxi < len(words):
               maxi = len(words)

        return maxi