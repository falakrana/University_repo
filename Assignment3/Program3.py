# Given two numbers x and y find the product using recursion


def recursive_multiple(x, y):
    if y == 0:
        return 0
    elif y < 0:
        print("Enter positive value of y!")
    else:
        return x + recursive_multiple(x, y - 1)
   


print(recursive_multiple(2, 4))
