'''
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
'''
num = 38
# num = list(str(num))
# while len(num) > 1:
#     sum = 0
#     for i in range(len(num)):
#         sum += int(num[i])
#     num = list(str(sum))
# ans = int(''.join(num))
if num == 0:
    print(0)
elif num % 9 == 0:
    print(9)
else:
    print(num%9)
