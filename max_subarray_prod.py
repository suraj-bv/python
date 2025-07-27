class Solution:
    def maxProduct(self,arr):
        if not arr:
            return 0
		
        max_prod = min_prod = result = arr[0]
		
        for num in arr[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
		        
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
		    
            result = max(result, max_prod)
		    
        return result
		    