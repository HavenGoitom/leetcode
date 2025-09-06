'''
Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''
address = "1.1.1.1"
parts = address.split(".")
joined = "[.]".join(parts)
print(joined)