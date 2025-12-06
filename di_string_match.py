class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        ans = []

        for ch in s:
            if ch == 'I':
                ans.append(low)
                low += 1
            else: # ch == 'D'
                ans.append(high)
                high -= 1
        ans.append(low) # low == high here

        return ans
        