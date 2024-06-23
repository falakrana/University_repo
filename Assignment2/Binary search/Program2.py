# Program 2: Binary search in 2D matrix.



def binarysearch_matrix(matrix, target):
    if not matrix:
        return False
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False
    
    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 43
print(binarysearch_matrix(matrix, target))