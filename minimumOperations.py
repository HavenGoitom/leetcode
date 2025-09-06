'''
Input: nums = [1,2,3,4]
Output: 3
Explanation:
All array elements can be made divisible by 3 using 3 operations:
Subtract 1 from 1.
Add 1 to 2.
Subtract 1 from 4.
Example 2:
Input: nums = [3,6,9]
Output: 0'''
nums = [3,6,9]
count = 0
for num in nums:
    if num % 3 == 0:
        continue
    if (num - 1)% 3 == 0:
        count +=1
    elif (num + 1)% 3 == 0:
        count +=1
print(count)