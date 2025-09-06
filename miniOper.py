'''
Input: nums = [2,11,10,1,3], k = 10
Output: 3
Explanation: After one operation, nums becomes equal to [2, 11, 10, 3].
After two operations, nums becomes equal to [11, 10, 3].
After three operations, nums becomes equal to [11, 10].
At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
It can be shown that 3 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.'''
nums = [2,11,10,1,3]
k = 10
count = 0
done = False
while not done:
    done = True 
    smallest = None
    for n in nums:
        if n < k:
            done = False
            if smallest is None or n < smallest:
                smallest = n
    if smallest is not None:
        nums.remove(smallest)
        count += 1

print(count)


