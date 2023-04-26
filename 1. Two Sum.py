class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums = nums
        self.target = target

        solve = []
        for i in range(0, len(nums)-1):
            for j in range(1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    solve.append(i)
                    solve.append(j)

                    return solve

