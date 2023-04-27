class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        self.digits = digits
        a = ''
        out = []
        for i in digits:
            a += str(i)
        for j in str(int(a)+1):
            out.append(int(j))
        return out


a = Solution()
print(a.plusOne([4,3,2,1]))

#out [4,3,2,2]