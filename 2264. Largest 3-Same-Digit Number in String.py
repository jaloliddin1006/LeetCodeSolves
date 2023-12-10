class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a = ''
        max_ = ''

        for i in num:
            if i in a:
                a += i
                if len(a) == 3:
                    max_ = max(max_, a)
            else:
                a = i
        
        return max_
        