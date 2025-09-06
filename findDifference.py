'''
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
'''
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
set1 = set(nums1)
set2 = set(nums2)
nums1_without2 = list(set1-set2)
nums2_without1 = list(set2-set1)
res = []
res.append(nums1_without2)
res.append(nums2_without1)
print(res)