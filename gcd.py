a = int(input('Enter the 1st number: '))

b = int(input('Enter the 2nd number: '))

def gcd(a, b):
    for i in range(1, a):
        if (a % i == 0) and (b % i == 0):
            gcd_value = i
    return gcd_value

print(f'GCD value :{gcd(a, b)}')