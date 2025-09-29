from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        max_altitude = 0

        for num in gain:
            height = height + num
            if max_altitude < height:
                max_altitude = height

        return max_altitude