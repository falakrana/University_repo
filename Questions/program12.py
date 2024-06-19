# Write a program to find the least common multiple (LCM) of two input numbers
"""
"""
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a / gcd(a, b)) * b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("LCM of", a, "and", b, "is", lcm(a, b))