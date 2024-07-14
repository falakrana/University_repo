# Sort Even and Odd Indices Independently


def sortEvenOdd(nums):
    odd_index = []
    for i in range(1, len(nums), 2):
        odd_index.append(nums[i])
    even_index = []
    for i in range(0, len(nums), 2):
        even_index.append(nums[i])

    odd_index.sort(reverse=True)
    even_index.sort()

    for i in range(1, len(nums), 2):
        nums[i] = odd_index.pop(0)
    for i in range(0, len(nums), 2):
        nums[i] = even_index.pop(0)

    return nums


nums = [4, 1, 2, 3]
print(sortEvenOdd(nums))
