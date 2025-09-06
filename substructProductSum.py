'''
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''
n = 4421
n = list(str(234))
sum = 0
product = 1
for num in n:
    sum += int(num)
    product *= int(num)
print(product-sum)