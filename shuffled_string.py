from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(s)
        for char, i in zip(s,indices):
            res[i] = char

        return "".join(res)