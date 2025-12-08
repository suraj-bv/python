class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        freq = Counter(text)

        b = freq.get('b', 0)
        a = freq.get('a', 0)
        l = freq.get('l', 0) // 2  # needs 2 l's
        o = freq.get('o', 0) // 2  # needs 2 o's
        n = freq.get('n', 0)

        return min(b, a, l, o, n)