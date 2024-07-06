# Compute sum of first N natural numbers using recursion


def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)


print(sum_of_natural_numbers(5))