matrix = matrix = [[1,2,3],[4,5,6]]
#[[1,4,7],[2,5,8],[3,6,9]]
n = len(matrix)
for i in range(0,n):
    for j in range(i+1,n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)