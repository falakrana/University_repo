# Write a program to generate the Fibonacci sequence up to a given number of terms

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter a number: "))
for i in range(n):
    print(fibonacci(i))
