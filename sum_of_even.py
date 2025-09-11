n = int(input())
arr = list(map(int, input().split()))

total = 0
for i in range(len(arr)):
  if arr[i] % 2 == 0:
    total += arr[i]

print(total)