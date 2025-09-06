'''
A mountain is called stable if the mountain just before it (if it exists) has a height strictly greater than threshold. Note that mountain 0 is not stable.
Return an array containing the indices of all stable mountains in any order.
Example 1:
Input: height = [1,2,3,4,5], threshold = 2
Output: [3,4]
'''
height = [1,2,3,4,5]
threshold = 2
res = []
for i in range(1, len(height)):
    if height[i-1] > threshold:
        res.append(i)
print(res)

