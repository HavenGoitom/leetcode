def applyOperations(nums):
    count = 0
    length = len(nums)
    for i in range(0,length-1):
        if nums[i] == nums[i+1] :
            nums[i] = nums[i] * 2
            nums[i+1] = 0 
    for i in range(count, length):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    for i in range(count, length):
        nums[i] = 0

    return nums
nums = [0,1]
print(applyOperations(nums))