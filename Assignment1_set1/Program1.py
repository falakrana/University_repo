"""
Write a program to check is a given number is
even or odd
positive, negative or zero
"""

def evenOrOdd(x):
    if x % 2 == 0:
        print(f"{x} is Even")
    else:
        print(f"{x} is Odd")
        
def positiveOrNegative(x):
    if x > 0:
        print(f"{x} is Positive")
    elif x == 0:
        print(f"{x} is zero")
    else:
        print(f"{x} is Negative")


n = int(input("Enter a number: "))
evenOrOdd(n)
positiveOrNegative(n)