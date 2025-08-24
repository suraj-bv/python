num = int(input('Enter the number: '))

def fibonacci(num):
    fibonnaci_series = [0, 1]
    if num <= 0:
        print("Invalid input")
        return
    elif num == 1 or num == 2:
        return fibonnaci_series
    else:
        while num > fibonnaci_series[-1]:
            fibonnaci_series.append(fibonnaci_series[- 1] + fibonnaci_series[- 2])
        fibonnaci_series.pop(-1)
        return fibonnaci_series

print(f'Number of fibonacci {fibonacci(num)}')


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)