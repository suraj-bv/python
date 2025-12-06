class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res  = s.split(" ")
        res  = res[:k]

        return " ".join(res)