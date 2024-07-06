def power_of_three(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return power_of_three(n // 3)

print(power_of_three(1))    
print(power_of_three(28))