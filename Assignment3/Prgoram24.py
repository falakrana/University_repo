# Find maximum and minimum of Array elements using recursion


def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], find_max(arr[1:]))


def find_min(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return min(arr[0], find_min(arr[1:]))


arr = [5, 3, 9, 1, 7]
print(find_max(arr))
print(find_min(arr))
