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
