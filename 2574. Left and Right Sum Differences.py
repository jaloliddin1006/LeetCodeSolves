class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        new_nums = [0] * n
        for i in range(n):
            left_sum = 0
            right_sum = 0
            for r in nums[i+1:]:
                right_sum += r
            for l in nums[:i]:
                left_sum += l
            new_nums[i] = abs(left_sum-right_sum)
        return new_nums
        


print(Solution().leftRigthDifference([10,4,8,3]))