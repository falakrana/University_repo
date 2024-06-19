# Write a program to find the greatest common divisor (GCD) of two input numbers

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


a = int(input("Enter a: "))
b = int(input("Enter b: "))



print(f"GCD of {a} and {b} is {gcd(a, b)}.")

        