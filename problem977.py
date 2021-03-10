def sortedSquares(self, nums: List[int]) -> List[int]:
    temp = [x * x for x in nums]
    temp.sort()
    return temp
