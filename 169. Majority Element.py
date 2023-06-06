class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n2 = len(nums)/2
        large = nums[0]
        for i in set(nums):
            if nums.count(i) > n2:
                return i
