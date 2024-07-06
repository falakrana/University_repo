# Compute the product of digits of a number using recursion

def digitProduct(n):
    if n == 0:
        return 1
    return n % 10 * digitProduct(n // 2)

print(digitProduct(145))