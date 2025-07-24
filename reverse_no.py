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



class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if (reversed_num > INT_MAX // 10) or (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num
# This code defines a class Solution with a method reverse that reverses an integer while checking for overflow conditions.
# It uses a two-pointer technique to reverse the digits and ensures that the reversed number does not exceed the 32-bit signed integer range.
# It also handles negative numbers by storing the sign and applying it at the end of the reversal process.