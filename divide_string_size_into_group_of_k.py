from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []
        i = 0

        while i < n:
            string = s[i:i+k]
            if len(string) < k:
                string += fill * (k - len(string))
            res.append(string)
            i += k

        return res