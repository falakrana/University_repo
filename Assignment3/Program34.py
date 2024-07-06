# Compute the GCD of two numbers using Euclidean Algorithm


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


num1 = 4
num2 = 18
print(gcd(num1, num2))
