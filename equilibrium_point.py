# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        total_sum = sum(arr)
        left_sum = 0
        
        for i, num in enumerate(arr):
            if left_sum == total_sum - num - left_sum:
                return i
            
            left_sum += num
            
        return -1