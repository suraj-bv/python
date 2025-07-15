num = int(input('Enter the number: '))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("The number of digits is:", count)