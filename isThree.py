def isThree(n):
    count = 1 
    for i in range(2,n+1):
        if n % i == 0:
            count += 1
    if count == 3:
            return True
    else:
        return False
n= 12
print(isThree(n))