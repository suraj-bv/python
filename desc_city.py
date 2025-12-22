class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Collect all cities that have outgoing paths
        starts = {path[0] for path in paths}

        # The destination will be the city that is never a starting city
        for a, b in paths:
            if b not in starts:
                return b