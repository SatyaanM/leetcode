from itertools import reduce


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:    #64ms 14.5mb
        list1 = [nums[x] for x in range(n)]
        list2 = [nums[x+n] for x in range(n)]
        list3 = []
        for x in range(n):
            list3.append(list1[x])
            list3.append(list2[x])
        return list3

    def shuffle2(self, nums: List[int], n: int) -> List[int]:   #56ms 14.5mb
        shuffled = []
        for x in range(n):
            shuffled.append(nums[x])
            shuffled.append(nums[x+n])
        return shuffled

    def shuffle3(self, nums: List[int], n: int) -> List[int]:   #72ms 14.7mb
        return reduce(lambda x, y: x + y, [[nums[x], nums[x+n]] for x in range(n)])
