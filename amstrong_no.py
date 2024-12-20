num = int(input('Enter the number: '))

def length(a):
    count = 0
    while a > 0:
        a = a // 10
        count+=1
    return count

print(length(num))

def amstrong(num):
    sum = 0
    temp = num
    l = length(num)
    while temp > 0:
        digit = temp % 10
        sum += digit ** l
        temp //= 10
    return sum == num

print(amstrong(num))