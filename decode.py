'''
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
'''
encoded = [6,2,7,3]
#[4,2,0,7,4]
first = 4
n = len(encoded)
arr = [first]
for i in range(n):
    first ^= encoded[i]
    arr.append(first)

print(arr)