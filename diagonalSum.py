def diagonalSum(mat):
    n = len(mat)
    pri = 0
    sec = 0
    for i in range(0, n):
        pri += mat[i][i]
        sec += mat[i][n-i-1]
    if n % 2 != 0:
        pri -= mat[n//2][n//2]
    return pri + sec

mat = [[1,2,3],
    [4,5,6],
    [7,8,9]]
print(diagonalSum(mat))