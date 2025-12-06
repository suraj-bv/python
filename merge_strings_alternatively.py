class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        j = 0
        m, n = len(word1), len(word2)

        while i < m and j < n:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        if i < m:
            res.append(word1[i:])

        if j < n:
            res.append(word2[j:])

        return "".join(res)