from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        left, right = s.split(':')
        col1, row1 = left[0], int(left[1:])
        col2, row2 = right[0], int(right[1:])
        
        res = []
        for c in range(ord(col1), ord(col2) + 1):
            col_char = chr(c)
            for r in range(row1, row2 + 1):
                res.append(f"{col_char}{r}")
        return res