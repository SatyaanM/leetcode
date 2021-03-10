def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = ""
    if len(strs) == 0:
        return prefix
    index = 0
    word = strs[0]

    while index < len(word):
        check = False
        ch = word[index]

        for string in strs:
            if index < len(string):
                if ch == string[index]:
                    check = True
                else:
                    return prefix
            else:
                return prefix
        if check is True:
            prefix += ch
        index += 1
    return prefix
