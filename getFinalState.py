'''
Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation	Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]
'''
nums = [2,1,3,5,6]
k = 5
multiplier = 2

for j in range(k):
    min = nums[0]
    index = 0
    for i in range(len(nums)):
        if nums[i]<min:
            min = nums[i]
            index = i
    nums[index]= multiplier*nums[index]
    print(nums)