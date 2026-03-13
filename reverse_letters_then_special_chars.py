class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        special = []
        for c in s:
            if c.isalnum():
                letters.append(c)
            else:
                special.append(c)

        letters.reverse()
        special.reverse()

        res = []
        li = 0
        si = 0
        for c in s:
            if c.isalnum():
                res.append(letters[li])
                li += 1
            else:
                res.append(special[si])
                si += 1

        return ''.join(res)