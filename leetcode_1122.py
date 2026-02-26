class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # Step 1: Count frequencies
        count = {}
        for x in arr1:
            count[x] = count.get(x, 0) + 1

        result = []

        # Step 2: Place elements from arr2
        for x in arr2:
            if x in count:
                result += [x] * count[x]
                del count[x]

        # Step 3: Remaining not in arr2 sorted ascending
        remaining = []
        for x in count:
            remaining += [x] * count[x]
        result += sorted(remaining)

        return result