class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0
        
        # for each column
        for j in range(len(strs[0])):
            # check if current column is lexicographically sorted
            for i in range(len(strs) - 1):
                if strs[i][j] > strs[i+1][j]:
                    delete_count += 1
                    break
        
        return delete_count