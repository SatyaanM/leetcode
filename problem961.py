class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for x in range(len(A)):
            nums = []
            while (A):
                num = A.pop()
                if num not in nums:
                    nums.append(num)
                else:
                    return num