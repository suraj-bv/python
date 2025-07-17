l = [1,5,15,2,35,7,8,11,9,66,4]

# n = len(l)

# def swap(a, b):
#     l[a] = l[a] + l[b]
#     l[b] = l[a] - l[b]
#     l[a] = l[a] - l[b]

# for i in range(n-1):
#     min = i
#     for j in range(i+1, n):
#         if l[min] > l[j]:
#             min = j
#     if min != i:
#         swap(min, i)
        
# print(l)

# print(f'Second largest element is {l[-2]}')

for i in range(len(l)-1):
    max = l[i]
    if max < l[i+1]:
        max = l[i+1]
    
print(max)