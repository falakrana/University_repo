# Write a program to calculate the sum of the first N natural numbers
def sumOfFirstNNaturalNumber(x):
    sum = 0
    for i in range(1, x + 1):
        sum += i
    print(f"Sum of first {x} natural numbers is {sum}.")


n = int(input("Enter a number: "))
sumOfFirstNNaturalNumber(n)