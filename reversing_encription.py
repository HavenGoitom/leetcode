def p4():
    length = int(input())
    encrypted = list(input())
    
    divisors = []
    for num in range(1, length + 1):
        if length % num == 0:
            divisors.append(num)
    
    divisors.sort()
    
    for div in divisors:
        encrypted[:div] = encrypted[:div][::-1]
    
    print(''.join(encrypted))

p4()
