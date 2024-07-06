# Find the nth number in a Fibonacci Series using Recursion

def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n - 1))