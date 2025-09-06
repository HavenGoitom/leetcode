nums = [1,2,3]
val = []
res = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            val.append(nums[i])
for num in val:
    res ^= num
print(res)