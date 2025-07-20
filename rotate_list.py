#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n 
        while d > 0:
            el = arr.pop(0)
            arr.append(el)
            d-=1
        
        return arr
    
    # the time complexity of this function is O(n*d) 
    # where n is the length of the array and d is the number of rotations.

    #we can optimize this function to O(n) time complexity using slicing
    def rotateArrOptimized(self, arr, d):
        n = len(arr)
        d = d % n
        return arr[d:] + arr[:d]