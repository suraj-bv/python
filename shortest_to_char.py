class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        INF = 10**9
        ans = [INF] * n

# Left -> right: distance to previous occurrence of c

        prev = -INF

        for i, ch in enumerate(s):
            if ch == c:
                prev = i

            ans[i] = i - prev

# Right -> left: distance to next occurrence of c

        next_pos = INF
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_pos = i

# min of current (distance to previous c) and distance to next c

            ans[i] = min(ans[i], next_pos - i)

        return ans