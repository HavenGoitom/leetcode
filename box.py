def p1():
    test_cases = int(input())
    result =[]
    for cases in range(test_cases):
        num_box = int(input())
        candies_original = input()
        candies_string = candies_original.split()
        candies = []
        for candy in candies_string:
            candies.append(int(candy))
        mini = min(candies)
        total = 0
        for i in range(num_box):
            total += candies[i] - mini
        result.append(total)
    for num in result:
        print(num)
p1()