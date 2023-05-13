class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = 0
        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            n += 1
        return n
    
print(Solution().numberOfSteps(8))