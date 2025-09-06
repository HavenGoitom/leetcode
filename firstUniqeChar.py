'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
'''
s = "leetcode"

char_count = {}
for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

for i in range(len(s)):
    if char_count[s[i]] == 1:
        print(i)
        break
else:
    print(-1)
