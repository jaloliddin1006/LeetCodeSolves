class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except: 
            for i in range(len(nums)-1):
                if target>nums[i] and target<nums[i+1]:
                    return i+1
            
            if nums[0]>target:
                return 0
            return len(nums)