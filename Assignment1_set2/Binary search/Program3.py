# Binary Search to find the floor and ceil of an element in an array


# Floor of an element is the largest element smaller than or equal to the element
# Ceil of an element is the smallest element greater than or equal to the element


def floor(n, nums):
    start = 0
    end = len(nums) - 1
    floor_value = None
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == n:
            return nums[mid]
        elif nums[mid] < n:
            floor_value = nums[mid]
            start = mid + 1
        else:
            end = mid - 1
    
    return floor_value

def ceil(n, nums):
    start = 0
    end = len(nums) - 1
    ceil_value = None
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == n:
            return nums[mid]
        elif nums[mid] > n:
            ceil_value = nums[mid]
            end = mid - 1
        else:
            start = mid + 1
    return ceil_value


nums = [1, 2, 4, 6, 8, 10]
print(floor(5, nums))
print(ceil(5, nums))

