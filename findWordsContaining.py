'''Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1'''
words = ["leet","code"]
x = "e"
res = []
for i in range(len(words)):
    words[i].split()
    for ch in words[i]:
        if ch == x:
            res.append(i)
            break
print(res)