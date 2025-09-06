'''
InputCopy
4
5 1
1 1 2 3 1
4 2
6 4 8 5
2 2
1 6
3 5
5 2 5
OutputCopy
2
6
-1
7
'''
def p3():
    test_case = int(input())
    res = []
    for cases in range (test_case):
        line = input().split()
        n = int(line[0])
        k = int(line[1])

        prices = []
        price_input = input().split()
        for i in range(n):
            prices.append(int(price_input[i]))
        max_list = []
        min_list =[]
        for i in range(n):
            max_list.append(prices[i] + k)
            min_list.append(prices[i] - k)
        if max(min_list) <= min(max_list):
            res.append(min(max_list))
        else:
            res.append(-1)
    for num in res:
        print(num)
p3()