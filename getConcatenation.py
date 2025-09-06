'''
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
'''
nums = [1,2,1]
nums.extend(nums)
print(nums)