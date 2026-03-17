class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = {}
        ans = -1

        for i, ch in enumerate(s):
            if ch not in first_index:
                first_index[ch] = i
            else:
                ans = max(ans, i - first_index[ch] - 1)

        return ans