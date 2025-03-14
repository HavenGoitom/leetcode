def isPerfectSquare(num):
    k=1
    while num>0:
        num = num - (2*k - 1)
        k = k+1

    return num == 0
num =17
print(isPerfectSquare(num))