# Write a program to find the sum of digits of an input number


def sumOfDigit(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    print(f"Sum of digits is {sum}.")
    
n = int(input("Enter a number: "))
sumOfDigit(n)