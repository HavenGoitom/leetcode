'''
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
'''
jewels = "z"
stones = "ZZ"
jewels = list(jewels)
stones = list(stones)
count = 0
for i in range(len(stones)):
    for j in range(len(jewels)):
        if stones[i] == jewels[j]:
            count +=1
            break

print(count)