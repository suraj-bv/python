import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False

        if target in (x, y, x + y):
            return True
        
        return target % math.gcd(x, y) == 0