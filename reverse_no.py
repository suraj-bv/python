def reverse(num):
    reversed_num = ''
    while(num!=0):
        digit = num % 10
        reversed_num += str(digit)
        num = num // 10
    return int(reversed_num)


num = int(input('Enter a number: '))

print('The reversed number is:', reverse(num))



def reverse_2(num):
    return int(str(num)[::-1])

num = int(input('Enter a number: '))

print('The reversed number is:', reverse_2(num))