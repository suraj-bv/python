num = int(input("Enter a number to check if it is perfect: "))

perfect_sum = 0

for i in range(1, num):
    if num % i == 0:
        perfect_sum += i

print(f"The sum of divisors of {num} is {perfect_sum}")

# Check if the number is perfect

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num//i
            
            i += 1
                    
        return total == num
    # this function checks if a number is perfect by summing its divisors and comparing it to the number itself.
    # its complexity is O(sqrt(n)), making it efficient for larger numbers.