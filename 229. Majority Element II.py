class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n2 = len(nums)/3
        majnums = []
        for i in set(nums):
            if nums.count(i) > n2:
                majnums.append(i)
        return majnums
