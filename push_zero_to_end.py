#User function Template for python3

class Solution:
	def pushZerosToEnd(self, arr):
		new_arr = []
		count = 0
		for i in range(len(arr)):
			if arr[i] != 0:
				new_arr.append(arr[i])
			else:
				count += 1

		new_arr.extend([0] * count)

		return new_arr
	

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)


# #User function Template for python3

# class Solution:
# 	def pushZerosToEnd(self,arr):
# 	    idx = 0
# 	    n = len(arr)
	    
# 	    for i in range(n):
# 	        if arr[i] != 0:
# 	            arr[idx] = arr[i]
# 	            idx += 1
	            
# 	    while idx < n:
# 	        arr[idx] = 0
# 	        idx += 1
	         
# 	    return arr