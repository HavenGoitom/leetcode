'''
numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
numRows = 5
res = []
for i in range(numRows):
    row = []
    for j in range(i+1):
        row.append(combination(i,j))
    res.append(row)
print(res)