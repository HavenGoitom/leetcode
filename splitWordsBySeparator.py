'''
Input: words = ["$easy$","$problem$"], separator = "$"
Output: ["easy","problem"]
Input: words = ["|||"], separator = "|"
Output: []
'''
words = ["$easy$","$problem$"]
separator = "$"

ans = []
for ch in words:
    splited = ch.split(separator)
    ans.append(splited)
res = []
for lst in ans:
    for word in lst:
        if word == "":
            continue
        res.append(word)

print(res)