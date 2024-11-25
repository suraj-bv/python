arr = [1, 3, 4, 5, 7, 8]
n = len(arr)

for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print(f'Reversed array: {arr}')