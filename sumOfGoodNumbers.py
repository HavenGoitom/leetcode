def sumOfGoodNumbers(nums,k):
    sum = 0
    for i in range(0, len(nums)):
        left_index = i - k 
        right_index = i + k
        if left_index >= 0 and right_index < len(nums):
            if nums[i] > nums[left_index] and nums[i] > nums[right_index]:
                sum += nums[i]
        elif left_index >= 0:
            if nums[i] > nums[left_index]:
                sum += nums[i]
        elif right_index >= 0:
            if nums[i] > nums[right_index]:
                sum += nums[i]
        else:
            sum += nums[i]    
    return sum

nums = [1,3,2,1,5,4]
k = 2
print(sumOfGoodNumbers(nums,k))