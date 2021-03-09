class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        # greatest = [[False]] * len(candies)
        greatest = [None] * len(candies)
        for kid in candies:
            if kid > max:
                max = kid
        for x in range(len(candies)):
            if (candies[x] + extraCandies) >= max:
                greatest[x] = True
            else:
                greatest[x] = False
        return greatest
