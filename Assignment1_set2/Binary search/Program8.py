#  Find First and Last Position of Element in Sorted Array
"""

Doubt

"""

def searchRange(nums, target):
    left = 0
    right = len(nums) - 1
    ans = []
    while left < right:
        if nums[left]  == target and nums[right] == target:
            ans.append(left)
            ans.append(right)
            break
        if nums[left] < target :
            left += 1
        if nums[right] > target :
            right -= 1
        if len(ans) == 0 :
            ans = [-1, -1]
            return ans
    return ans


nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))
                
                
        