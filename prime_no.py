n = int(input('Enter the no.: '))

def prime_no(n):
    if n < 2:
        print("No prime numbers")
        return
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

print(prime_no(n))