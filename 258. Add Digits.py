class Solution:
    def addDigits(self, num: int) -> int:
        self.num = num
        while num//10 != 0:
            x = 0

            for i in str(num):
                x += int(i)
            num = x
        return num
            
a = Solution()
print(a.addDigits(38))

# in: 38
# out: 2