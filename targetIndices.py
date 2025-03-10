def targetIndices(nums, target):
    indices = []
    sorted_nums = sorted(nums)
    for i in range(0 , len(nums)):
        if sorted_nums[i] == target:
            indices.append(i)
    return indices

nums = [1,2,5,2,3]
target = 2
print(targetIndices(nums, target))