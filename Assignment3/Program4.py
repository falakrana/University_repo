# Find the value of 'a' raised to the power 'b' using recursion


def a_pow_b(a, b):
    if b == 0:
        return 1
    elif b < 0:
        print("Enter positive value of b!")
    else:
        return a * a_pow_b(a, b - 1)



print(a_pow_b(2, 4))