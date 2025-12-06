class Solution:
    def countAsterisks(self, s: str) -> int:
        count_bar = 0
        count_star = 0
        
        for char in s:
            if char == '|':
                count_bar += 1
            if char == '*' and count_bar % 2 == 0:
                count_star += 1

        return count_star