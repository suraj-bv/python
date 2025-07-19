nums = [3, 0, 1, 5, 6, 2]

n = len(nums)
total_sum = (n * (n + 1)) / 2

missing_number = total_sum - sum(nums)
print(f"The missing number is: {int(missing_number)}")

