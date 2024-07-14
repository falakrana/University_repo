# Squares of a Sorted Array


def sortedSquares(nums):
    squares = [num * num for num in nums]
    
    squares.sort()
    
    return squares

nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)  