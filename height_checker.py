'''
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
'''
heights = [5,1,2,3,4]
orginal = heights[:]
heights.sort()
count = 0
for i in range(len(heights)):
    if orginal[i] != heights[i]:
        count += 1
print(count)