def categorize_box(length, width, height, mass):
    volume = length * width * height
    bulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9
    heavy = mass >= 100

    if bulky and heavy:
        return "Both"
    elif bulky:
        return "Bulky"
    elif heavy:
        return "Heavy"
    else:
        return "Neither"

print(categorize_box(10000, 100, 100, 99))   
print(categorize_box(100, 100, 100, 100))    
print(categorize_box(10000, 100, 100, 100))  
print(categorize_box(1, 1, 1, 1))            
