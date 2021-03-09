class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sums.append(nums[0])
        for x in range(1, len(nums)):
            sums.append(sums[x - 1] + nums[x])

        return sums
