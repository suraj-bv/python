def search(a,k):
    low = 0
    high = len(a) - 1

    while low <= high :
        mid = (low + high)//2
        if k == a[mid]:
            print(f"Key element found at index {mid+1}")
            return
        elif k > a[mid]:
            low = mid + 1
        elif k < a[mid]:
            high = mid - 1
    print('Key element not found')


l = []

n = int(input('Enter the no of elements in the list :'))

print('Enter the elements in the list :')

for i in range(n):
    a = int(input())
    l.append(a)

key = int(input('Enter the key element :'))

search(l,key)



from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

        return -1
