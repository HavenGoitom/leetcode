def p2():
    test_cases = int(input())
    result = []

    for cases in len(test_cases):
        a = input()
        i = 0
        for i in a:
            if a[i] == a[i+1]:
                result.append(a[i])
                i = i+1
    for _ in result:
        print(_)
p2()