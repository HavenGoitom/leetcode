'''Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.'''
s = "abcd"
t = "abecd"
s = list(s)
t = list(t)
for ch in t:
    if ch in s:
        s.remove(ch)
    else:
        print(ch)
        break
