'''nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28'''
nums = [1,3]
ans = []
for i in range(len(nums)+1):
    for j in range(i+1, len(nums)):
        ans.append(nums[i]^nums[j])
xor = 0
for num in nums:
    xor ^= num
ans.append(xor)
sum = 0
for num in ans:
    sum += num
print(sum)