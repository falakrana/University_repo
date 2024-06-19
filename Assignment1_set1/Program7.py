# Write a program to check if an input string is a palindrome


def palindrome(s):
    return s[::-1]

s = input("Enter a string: ")
if s == palindrome(s):
    print("String is palindrome")
else:
    print("String is not palindrome")