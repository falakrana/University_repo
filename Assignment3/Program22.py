# Find sum of Array elements using recursion


def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])


arr = [1, 2, 73, 42, 345]
print(sum_array(arr))
