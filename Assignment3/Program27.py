# Perform binary search using recursion


def binarysearch(arr, target, start, end):
    # Base calculation:
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binarysearch(arr, target, start, mid - 1)
    else:
        return binarysearch(arr, target, mid + 1, end)


nums = [-1,0,3,5,9,12], 
target = 9

print(binarysearch(nums, target))