# Sort Colors:


def sortColors( nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
nums = [2,0,2,1,1,0]

print(nums)
sortColors(nums)
print(nums)