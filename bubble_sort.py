# reading the no. of elements
n = int(input('Enter the no. of elements: '))

# initializing an empty list
l = []

# reading all the elements of the list
for i in range(n):
    l.append(int(input('Enter the elements: ')))

# sorting using bubble sort
for i in range(n-1):
    for j in range(n-1-i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp

print(f'Sorted list is {l}')