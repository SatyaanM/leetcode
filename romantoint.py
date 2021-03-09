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


print(romanToInt('', "LXVIII"))
