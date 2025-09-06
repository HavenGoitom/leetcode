'''You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages.

Example 1:

Input: nums = [7,8,3,4,15,13,4,1]

Output: 5.5'''
nums = [7,8,3,4,15,13,4,1]
res = []
while len(nums) > 1:
    max_num = max(nums)
    min_num = min(nums)
    res.append((max_num + min_num)/2.0)
    nums.remove(max_num)
    nums.remove(min_num)
print(min(res))