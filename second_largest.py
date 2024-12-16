l = [1,5,2,5,7,8,11,9,15,66]

n = len(l)

for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if l[min] > l[j]:
            min = j
    if min != i:
        l[min] ,l[i] = l[i], l[min]
        
print(l)

print(f'Second largest element is {l[-2]}')