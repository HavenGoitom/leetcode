def count_even_numbers(digits):
    even_digits = []  
    for d in digits:
        if d % 2 == 0:
            even_digits.append(d)

    count = 0

    for last_digit in even_digits:  
        for first_digit in digits:  
            if first_digit == 0:
                continue  
            if first_digit == last_digit:
                continue  
            
            for second_digit in digits:  
                if second_digit == first_digit or second_digit == last_digit:
                    continue  

                count += 1  

    return count

digits = [1, 2, 3, 4]
print(count_even_numbers(digits))  # Output: 12
