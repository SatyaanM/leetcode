class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] == nums[y] and x == y:
                    continue
                else:
                    if nums[x] + nums[y] == target:
                        list.append(x)
                        list.append(y)
                        return list
