'''
Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
'''
nums = [-1,10,6,7,-7,1]
n = len(nums)
res=[]
for num in nums:
    if -num in nums:
        res.append(num)

if res:
    print(max(res))
else:
    print(-1)
    