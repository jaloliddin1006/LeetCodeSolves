class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        # O'zidan takrorlanuvchi elementlarini olib tashlash
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))