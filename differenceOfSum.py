'''
Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
'''
nums = [1,15,6,3]
element_sum = sum(nums)
digit_sum = 0
for ch in nums:
    splited_ch = list(str(ch))
    for num in splited_ch:
        digit_sum += int(num)
res = abs(element_sum - digit_sum)
print(res)