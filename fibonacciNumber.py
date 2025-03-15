def fibonacciNumber(num):
    fibo_nums = {"f0": 0 , "f1": 1}
    for i in range(2,num+1):
        fibo_nums[f"f{i}"] = fibo_nums[f"f{i-1}"] + fibo_nums[f"f{i-2}"]
    return fibo_nums[f"f{num}"]

n = 8
print(fibonacciNumber(n))

