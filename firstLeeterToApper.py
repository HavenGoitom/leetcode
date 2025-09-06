'''
Input: s = "abccbaacz"
Output: "c"
'''
s = "abccbaacz"
s = list(s)
n = len(s)
indexes = []
for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j]:
            indexes.append(j)
first_index = min(indexes)
print(s[first_index])