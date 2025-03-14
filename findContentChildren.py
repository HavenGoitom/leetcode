def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    child = 0
    cookie = 0
    while child< len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            count += 1
            child += 1
        cookie +=1
        
    return count
g = [10,9,8,7]
s = [5,6,7,8]
print(findContentChildren(g,s))