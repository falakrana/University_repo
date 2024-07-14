def findTargetIndices(nums):
    sorted_nums = sorted(nums)

    index_map = {}

    for i in range(len(nums)):
        num = nums[i]
        index_map[num] = i

    target_indices = []

    for num in sorted_nums:
        target_indices.append(index_map[num])

    return target_indices


nums = [3, 1, 4, 2, 10]
indices = findTargetIndices(nums)
print(indices)
