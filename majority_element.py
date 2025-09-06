'''
Input: nums = [2,2,1,1,1,2,2]
Output: 2

nums = [1,1,2,1]
length = len(nums)
for i in range(length):
    count = 1
    for j in range(i+1, length):
        if nums[i] == nums[j]:
            count += 1
    if count > length/2:
        res = nums[i]
        break
'''
nums = [1,1,2,1]
candidate = 0
count = 0
for num in nums:
    if count == 0:
        candidate = num
    if candidate == num:
        count += 1
    else:
        count -= 1
print(candidate)