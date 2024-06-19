# Write a program to check if an input number is an Armstrong number

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_digits == n

n = int(input("Enter a number: "))
if is_armstrong(n):
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")