class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s = [nums.pop(0)]
        for i in nums:
            s.append(i+s[-1])
        return s

