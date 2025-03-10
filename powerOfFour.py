def isPowerOfFour(n):
    while n > 1:
        if n % 4 != 0:
            return False
        n = n / 4
    return n == 1

try:
    user_input = int(input("Enter a number: "))
    while True:
        try:
            print(isPowerOfFour(user_input))
            break
        except ValueError:
            print("Please enter a valid integer.")
except ValueError:
    print("Please enter a valid integer.")
