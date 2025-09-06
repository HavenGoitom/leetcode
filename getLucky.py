def letter_to_number(ch):
    return ord(ch) - ord('a') + 1
s = "zbax"
k = 2
s = list(s)
res = []
for ch in s:
    num = letter_to_number(ch)
    res.append(str(num))
ans = int(''.join(res))
print(ans)
# tran = list(str(ans))
for i in range(k):
    digit_sum = 0
    for digit in str(ans):
        digit_sum += int(digit)
    ans = digit_sum
print(ans)