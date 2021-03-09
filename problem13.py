#efficient method
def romanToInt(self, s: str) -> int:
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for x in range(len(s)-1):
        if dictionary[s[x]] < dictionary[s[x+1]]:
            num -= dictionary[s[x]]
        if dictionary[s[x]] >= dictionary[s[x+1]]:
            num += dictionary[s[x]]
    num += dictionary[s[-1]]
    return num



#inefficient method
#     def romanToInt(self, s: str) -> int:
#         dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         num = 0
#         x = 0
#         while x < len(s)-1:
#             if s[x] == 'I':
#                 if s[x + 1] == 'V' or s[x + 1] == 'X':
#                     num += (dictionary[s[x + 1]] - dictionary[s[x]])
#                     x += 2
#                 else:
#                     num += 1
#                     x += 1
#             elif s[x] == 'X':
#                 if s[x + 1] == 'L' or s[x + 1] == 'C':
#                     num += (dictionary[s[x + 1]] - dictionary[s[x]])
#                     x += 2
#                 else:
#                     num += 10
#                     x += 1
#             elif s[x] == 'C':
#                 if s[x + 1] == 'D' or s[x + 1] == 'M':
#                     num += (dictionary[s[x + 1]] - dictionary[s[x]])
#                     x += 2
#                 else:
#                     num += 100
#                     x += 1
#             else:
#                 num += dictionary[s[x]]
#                 x += 1
#             print(num)
#         if x == len(s)-1:
#             num += dictionary[s[x]]
#             x += 1
#             print(num)
#         return num
