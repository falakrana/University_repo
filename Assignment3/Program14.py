# Power of Two


def power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return power_of_two(n // 2)


print(power_of_two(1))    # Output: True (2^0)
print(power_of_two(14))