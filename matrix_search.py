#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		for rows in mat:
		    if x in rows:
		        return True
		
		return False