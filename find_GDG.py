def findGDG(nums):
    even_numbers = 0
    mx = max(nums)
    mn = min(nums)
    GDG = 1
    new_list = [mn, mx]
    for i in range(1,mn + 1):
        if mn%i == 0 and mx%i == 0:
            GDG = i
    return GDG  
nums = [3,4,5,2,9]
print(findGDG(nums))

