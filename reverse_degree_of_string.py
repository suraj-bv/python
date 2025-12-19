class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            # 'z' - c gives 0 for 'z', 25 for 'a'; add 1 for range 1..26
            rev_val = (ord('z') - ord(c) + 1)
            ans += rev_val * (i + 1)
        return ans