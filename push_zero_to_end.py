#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
	    new_arr = []
	    count = 0
    	for i in range(len(arr)):
    	    if arr[i] != 0:
    	        new_arr.append(arr[i])
    	    else:
    	        count+=1
    	
    	new_arr.extend([0] * count)
    	
    	return new_arr