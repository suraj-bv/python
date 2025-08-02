class Solution:
    def kthMissing(self, arr, k):
        # code here
        missing = []
        i = 1
        idx = 0
        
        while len(missing) < k:
            if idx < len(arr) and arr[idx] == i:
                idx += 1
            else:
                missing.append(i)
            i += 1
            
        return missing[-1]