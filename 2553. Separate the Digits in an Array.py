class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        new = []
        for i in nums:
            n = str(i)
            for j in n: 
                new.append(int(j))
        return new

print(Solution().separateDigits([123, 23]))
