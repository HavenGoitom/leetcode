'''
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
'''
word1 = ["a", "cb"]
word2 = ["ab", "c"]
conc1 = ''
conc2 = ''
for word in word1:
    conc1 += word
for word in word1:
    conc2 += word
print(conc2)
print(conc1)
if conc1 == conc2:
    print(True)
else:
    print(False)