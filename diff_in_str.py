class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sSum, tSum = 0, 0
        for char1 in s:
            sSum += ord(char1)

        for char2 in t:
            tSum += ord(char2)

        char = tSum - sSum

        return chr(char)