# Find Target Indices After Sorting Array

def targetIndices(nums, target):
    nums.sort()
    ans_list = []
    count = -1
    for i in nums:
        count+=1
        if i == target:
            # ans_list.append(nums.index(i))
            ans_list.append(count)
    return ans_list


nums = [1,2,5,2,3]
target = 3
print(targetIndices(nums, target))