import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        nums = []
        sum = 0
        x = 1
        
        while x <= math.sqrt(num):
            if num % x == 0:
                nums.append(x)
            x += 1
        length = len(nums)
        
        for x in range(1, length):
            nums.append(num / nums[x])
            
        for x in nums:
            sum += x
        
        if sum == num and sum != 1:
            return True
        else:
            return False