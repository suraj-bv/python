class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []
        
        # Gather indices where s1 and s2 differ
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False
        
        # No differences → already equal
        if len(diffs) == 0:
            return True
        
        # Exactly 2 differences → check swap condition
        if len(diffs) == 2:
            i, j = diffs
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        # Only 1 mismatch → can't fix with one swap
        return False