def average(array):
    array2 = set(array)
    n = len(array2)
    total = 0
    for i in range (n):
        total+=array[i]
    avg = total / n
    return avg

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements separated by spaces: ").split()))
result = average(arr)
print(f"The average of unique numbers is: {result}")