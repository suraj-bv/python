from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            res = word.split(separator)
            for i in res:
                if i:
                    result.append(i)

        return result
