'''
Input: rowIndex = 3
Output: [1,3,3,1]
'''
rowIndex = 3
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
res = []
for i in range(rowIndex+1):
        res.append(combination(rowIndex,i))
print(res)