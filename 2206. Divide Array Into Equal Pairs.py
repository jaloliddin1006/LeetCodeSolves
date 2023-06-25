class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mynums = set(nums)
        for i in mynums:
            if nums.count(i) % 2 != 0:
                return False
        return True
