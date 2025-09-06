'''
A pair (i, j) is called good if nums1[i] is divisible 
by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1
Output: 5
Explanation:
The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).'''

nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
count = 0
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] % (nums2[j] * k) == 0:
            count += 1
print(count)