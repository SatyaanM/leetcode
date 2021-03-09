class Solution:
    def reverse(self, x: int) -> int:
        limit = 2147483648
        num = str(abs(x))[::-1]
        if x >= 0:
            num = int(num)
        else:
            num = int("-" + num)
        if abs(num) > limit:
            return 0
        else:
            return num