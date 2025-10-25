from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        result = []
        for person in order:
            if person in friends_set:
                result.append(person)
        return result