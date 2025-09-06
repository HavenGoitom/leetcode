'''

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
Example 1:
Input: n = 10, m = 3
Output: 19
We return 37 - 18 = 19 as the answer.
'''
n = 10
m = 3
sumN = 0
sumM = 0
for num in range(1, n+1):
    if num % m != 0:
        sumN += num
    if num % m == 0:
        sumM += num
print(sumN - sumM)