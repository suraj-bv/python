from collections import Counter
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Build frequency of letters in licensePlate (ignore non-letters)
        plate_letters = [ch.lower() for ch in licensePlate if ch.isalpha()]
        required = Counter(plate_letters)
        
        best = None
        for w in words:
            wcount = Counter(w.lower())
            # Check if w covers required counts
            covers = True
            for ch, cnt in required.items():
                if wcount.get(ch, 0) < cnt:
                    covers = False
                    break
            if covers:
                if best is None or len(w) < len(best):
                    best = w
        return best