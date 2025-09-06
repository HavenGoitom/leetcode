def contain_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

    
nums = [1,2,3,4,4]
print(contain_duplicates(nums))