def numIdenticalPairs(self, nums: List[int]) -> int:
    pairs = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] == nums[j]:
                pairs += 1
    return pairs
