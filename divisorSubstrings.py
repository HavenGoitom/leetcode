'''
Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.
'''
#thing[start:stop:step]
num = 2
k = 1
num_str = str(num)
ans = []
for i in range(len(num_str)-k+1): # i still dont understand the need of adding -k
    ans.append(num_str[i:i+k])
k = 0
for i in range(len(ans)):
    if int(ans[i]) == 0:
        continue
    if num % int(ans[i]) == 0:
        k += 1
print(k)
