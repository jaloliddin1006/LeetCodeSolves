class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if (nums[i+2]+nums[i+1]>nums[i]):
                return nums[i+2]+nums[i+1]+nums[i]
    

print(Solution().largestPerimeter([1,2,4, 2, 1]))