'''
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
'''
s = "codeleet"
s = list(s)
indices = [4,5,6,7,0,2,1,3]
s_list = list(s)
res = [''] * len(s_list)
for i in range(len(s_list)):
    res[indices[i]] = s_list[i]

print("".join(s))  



