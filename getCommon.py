nums1 = [1,2,3,4]
nums2 = [2,3,6]
set1 = set(nums1)
set2 = set(nums2)
res =set1 & set2
if res:
    val = min(res)
else:
    val = None
print(val)