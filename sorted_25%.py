'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

'''
arr = [1,1]
length = len(arr)

for i in range(length):
    count = 1
    for j in range(i+1, length):
        if arr[i] == arr[j]:
            count += 1
    if count > 25/100 * length:
        res = arr[i]
        break
print(res)