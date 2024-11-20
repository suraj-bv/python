# reading the no. of elements
n = int(input('Enter the no. of elements: '))

# initializing an empty list
l = []

# reading all the elements of the list
for i in range(n):
    l.append(int(input('Enter the elements: ')))


for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if l[min] > l[j]:
            min = j
    if min != i:
        l[min] ,l[i] = l[i], l[min]

print(f"Sorted list is {l}")