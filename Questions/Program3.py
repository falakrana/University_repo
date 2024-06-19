# Write a program to calculate the factorial of a given number

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


n = int(input("Enter a number: "))
print(factorial(n))