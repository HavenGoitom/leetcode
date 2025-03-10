def smallestEqual(nums):
    for i in range(0, len(nums)):
        if i % 10 == nums[i]:
            index = i
            break
        else:
            index = -1
    return index
nums = [4,3,2,1]
print(smallestEqual(nums))

