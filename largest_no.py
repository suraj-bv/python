n = int(input('Enter the no. of items in the list: '))

l = [int(input('Enter the item of the list: ')) for i in range(n)]

def largest_no(li):
    largest = li[0]
    for i in range(1, n):
        if li[i] > largest:
            largest = li[i]
    return largest

print(f'Largest no in the list is :{largest_no(l)}')