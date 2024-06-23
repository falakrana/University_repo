# Valid Perfect Square
from math import sqrt
def isPerfectSquare(num):
    root = int(sqrt(num))
    return root * root == num
    

nums = 15
print(isPerfectSquare(nums))