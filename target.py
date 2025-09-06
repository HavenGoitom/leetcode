nums = [2,5,5,11]
target = 10
#Output: [1,2]
res = []
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == target:
            res.append(i)
            res.append(j)
            break
    if res:
        break
print(res)