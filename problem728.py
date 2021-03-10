def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    nums = []
    for x in range(left, right + 1):
        check = False
        for digit in str(x):
            if int(digit) == 0:
                check = False
                break
            elif x % int(digit) == 0:
                check = True
            else:
                check = False
                break
        if check:
            nums.append(x)
    return nums