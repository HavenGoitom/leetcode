'''
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
'''
digits = [4,3,2,1]
strings = []
for num in digits:
    strings.append(str(num))
final = str(int(''.join(strings)) + 1)
res = []
for ch in final:
    res.append(int(ch))
print(res)