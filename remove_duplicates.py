def remove_duplicates(input_list):
    unique_items = []
    for item in input_list:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

list = []
n= int(input('Enter the no. of Elements: '))
print('Enter the list Elements: ')
for i in range (n):
    no=int(input())
    list.append(no)
unique_list = remove_duplicates(list)
print("List without duplicates :", unique_list)


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    # this code is efficient and checks for duplicates in a list
    # it uses a set to track seen numbers, which allows for O(1) average time complexity for lookups.
    # the whole code is O(n) in time complexity, where n is the number of elements in the list.
    # this code is more efficient than the previous one as it avoids nested loops.
