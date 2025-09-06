'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
s = "A man, a plan, a canal: Panama"
cleaned = ""

for ch in s:
    if ch.isalnum():
        cleaned += ch.lower()

if cleaned == cleaned[::-1]:
    print(True)
else:
    print(False)