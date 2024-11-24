n = int(input('Enter the no. of elements: '))

l = []

for i in range(n):
    l.append(int(input('Enter the elements: ')))

for i in range(n-1):
    for j in range(n-1-i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp

print(f'Sorted list is {l}')