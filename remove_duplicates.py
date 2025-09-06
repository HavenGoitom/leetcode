'''
Input
nums =[1,1,2]
Output= [1,2]
'''
nums = [1,1,2,2]
length = len(nums)
res = []
for i in range(length):
    if nums[i] in res:
        continue
    res.append(nums[i])
print(len(res))