'''
Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = 
[3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
'''
nums =[[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
res = set(nums[0])
for num in nums:
    res &= set(num)
val = list(res)
val.sort()
print(val)