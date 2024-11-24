def factorial(n):
    if n == 1:
        return 1
    else:
        ans = n * factorial(n-1)
    return ans 


n = int(input('Enter the number: '))
ans = factorial(n)
print(f'The factorial of {n} is {ans}')
