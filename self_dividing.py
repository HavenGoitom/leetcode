res = []
lst = list(range(22 + 1))
for num in lst:
    if num == 0:
        continue
    num1 = list(str(num))
    flag = False
    count = 0
    for i in range(len(num1)):
        if num1[i] != '0' and num % int(num1[i]) == 0:
            count +=1
    if len(num1) == count:
        res.append(num)
print(res)