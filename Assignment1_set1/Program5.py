# Write a program to check if an input number is prime or not
def check_prime(n):
    flag = 0
    for i in range(1, n + 1):
        if n % i == 0:
            flag += 1
    
    if flag == 2:
        print("Prime")
    else:
        print("Not Prime")
        
n = int(input("Enter a number: "))
check_prime(n)