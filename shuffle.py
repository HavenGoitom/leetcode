'''
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
'''
nums = [1,2,3,4,4,3,2,1]
n = 4
arr1 = nums[:n]
arr2 = nums[n:]
res = []
for i in range(n):
    res.append(arr1[i])
    res.append(arr2[i])
print(res)
    