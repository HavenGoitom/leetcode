def singleNumber(my_list):
    result = 0
    for num in my_list:
        result ^= num  
    return result

my_list = [4, 1, 2, 1, 2]
print(singleNumber(my_list))  
