'''Input: s = "abc", t = "bac"
Output: 2
Explanation:
For s = "abc" and t = "bac", the permutation difference of s and t is equal to the sum of:

The absolute difference between the index of the occurrence of "a" in s and the index of the occurrence of "a" in t.
The absolute difference between the index of the occurrence of "b" in s and the index of the occurrence of "b" in t.
The absolute difference between the index of the occurrence of "c" in s and the index of the occurrence of "c" in t.
That is, the permutation difference between s and t is equal to |0 - 1| + |1 - 0| + |2 - 2| = 2.'''
s = "abc"
t = "bac"
s = list(s)
t = list(t)
sum = 0
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            sum += abs((i-j))
print(sum)