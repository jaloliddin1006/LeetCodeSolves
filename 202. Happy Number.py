class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n==7:
            return True
        num = str(n)
        while len(num) > 1:
            a = 0
            for i in num:
                a += int(i)*int(i)
            if a == 1 or a == 7:
                return True
            num = str(a)

        return False




print(Solution().isHappy(1111111))

