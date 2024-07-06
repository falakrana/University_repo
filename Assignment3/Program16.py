def power_of_four(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    return power_of_four(n // 4)


print(power_of_four(1))
print(power_of_four(18))
