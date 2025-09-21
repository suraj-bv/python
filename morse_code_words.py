from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        
        transformations = set()
        
        for word in words:
            code = "".join(morseCode[ord(ch) - ord('a')] for ch in word)
            transformations.add(code)

        return len(transformations)
    
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# 'a' maps to ".-", 'b' maps to "-...", 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below