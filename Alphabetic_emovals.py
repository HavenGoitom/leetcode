# '''
# InputCopy
# 15 3
# cccaabababaccbc
# OutputCopy
# cccbbabaccbc
# '''
# def p5():
#     line = input().split()
#     length = int(line[0])
#     remove = int(line[1])
#     alphabets = list(input())
#     for _ in range(remove):
#         smallest = min(alphabets)
#         alphabets.remove(smallest)
#     print(''.join(alphabets))
# p5()
# #  for i in range(remove):
# #         smallest = min(alphabets)
# #         alphabets.remove(smallest)
def p5():
    inputs = input().split()
    length = int(inputs[0])
    to_delete = int(inputs[1])
    text = input()

    letters_to_remove = {}
    for char in sorted(text):
        if to_delete == 0:
            break
        if char in letters_to_remove:
            letters_to_remove[char] += 1
        else:
            letters_to_remove[char] = 1
        to_delete -= 1

    final_chars = []
    for char in text:
        if char in letters_to_remove and letters_to_remove[char] > 0:
            letters_to_remove[char] -= 1
        else:
            final_chars.append(char)

    print(''.join(final_chars))

p5()
