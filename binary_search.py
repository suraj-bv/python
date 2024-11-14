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