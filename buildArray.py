'''
ans[i] = nums[nums[i]]
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
'''
nums = [0,2,1,5,3,4]
ans = []
for i in range(len(nums)):
    num =  nums[nums[i]]
    ans.append(num)
print(ans)