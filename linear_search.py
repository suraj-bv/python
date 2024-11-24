n = int(input('Enter the no. of elements: '))

l = [int(input('Enter the elements of the list: ')) for i in range(n)]
key = int(input('Enter the key element to search: '))

i = 0

while i<n:
    if l[i] == key:
        print(f'Key element found at index {i+1}')
        break
    else:
        i+=1

print('Key element not found')