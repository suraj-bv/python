class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []
        s = str(n)
        count = 0

        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
            count += 1
            if count % 3 == 0 and i != 0:
                res.append('.')

        return ''.join(res[::-1])