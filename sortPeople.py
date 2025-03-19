def sortPeople(names, heights):
    n = len(names)
    for i in range(n):
        for j in range(n-i-1): 
            if heights[j] < heights[j+1]: 
                heights[j], heights[j+1] = heights[j+1], heights[j]
                names[j], names[j+1] = names[j+1], names[j]
    
    return names

names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
print(sortPeople(names, heights))  
