class Solution:
    def commonChars(self, words):
        min_freq = [float('inf')] * 26
        
        for word in words:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            for i in range(26):
                min_freq[i] = min(min_freq[i], freq[i])
        
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * min_freq[i])
        
        return result