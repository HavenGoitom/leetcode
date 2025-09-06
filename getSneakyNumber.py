'''
Input: nums = [0,1,1,0]
Output: [0,1]
'''
nums = [0,1,1,0]
res = []
for i in range(len(nums)):
    for j in range(i+1 , len(nums)):
        if nums[i]== nums[j]:
            res.append(nums[i])
print(res)