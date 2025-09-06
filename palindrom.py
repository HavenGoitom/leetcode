'''
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''
x = 121

rev = int(str(x)[::-1])
if x == rev:
    print('palin')