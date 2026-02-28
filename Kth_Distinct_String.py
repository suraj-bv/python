from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        
        for i in range(len(arr)):
            if arr[i] not in (arr[:i] + arr[i+1:]):
                res.append(arr[i])

        return res[k-1] if k <= len(res) else ""