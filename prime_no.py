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

# Optimized version using Sieve of Eratosthenes
# This version uses a more efficient algorithm to find all prime numbers up to n.
# This divides the range into smaller segments and marks non-prime numbers.
# 
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)