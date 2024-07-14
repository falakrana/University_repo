# The K Weakest Rows in a Matrix


def kWeakestRows(mat, k):
    strength = []
    
    for i in range(len(mat)):
        soldier_count = sum(mat[i])
        strength.append((soldier_count, i))
    
    strength.sort()
    
    weakest_rows = []
    for i in range(k):
        weakest_rows.append(strength[i][1])

    
    return weakest_rows

mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3
print(kWeakestRows(mat, k)) 
