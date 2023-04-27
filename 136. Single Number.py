class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            k = nums.count(i)
            if k == 1:
                break
        return i
    

print(Solution().singleNumber([1, 3, 1]))
#out:3