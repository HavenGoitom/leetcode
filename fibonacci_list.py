def fibonacci(N):
    f = [0, 1]
    if N == 0:
        return f[0]
    if N == 1:
        return f[1]
    
    for i in range(1, N):
        f[0], f[1] = f[1], sum(f)
    
    return f[1]

# Example usage:
# N = 8
# print(fibonacci(N))
