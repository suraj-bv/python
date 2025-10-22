from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        
        people.sort(reverse=True)
        
        result = [name for height, name in people]
        
        return result
