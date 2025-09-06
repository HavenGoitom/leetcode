'''Input: nums = [4,1,4,0,3,5]
Output: 2
Explanation:
1. Remove 0 and 5, and the average is (0 + 5) / 2 = 2.5. Now, nums = [4,1,4,3].
2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5, and nums = [4,3].
3. Remove 3 and 4, and the average is (3 + 4) / 2 = 3.5.
Since there are 2 distinct numbers among 2.5, 2.5, and 3.5, we return 2.'''
nums = [4,1,4,0,3,5]
res = []
while len(nums) > 1:
    max_num = max(nums)
    min_num = min(nums)
    res.append((max_num + min_num)/2)
    nums.remove(max_num)
    nums.remove(min_num)
print(len(set(res)))