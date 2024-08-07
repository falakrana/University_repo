# Compute the sum of digits of a number using recursion


def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(n // 10)


print(sum_of_digit(2280))
