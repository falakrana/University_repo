# Write a program to find factors of a given number

def countFactors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end = " ")
            
n = int(input("Enter a number: "))
countFactors(n)