class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums)<3:
            return True

        a = -1 if nums[0] < nums[1]  else 1 if nums[0] > nums[1]  else 0

        for i in range(1, len(nums)-1):
            c = -1 if nums[i] < nums[i + 1] else 1 if nums[i] > nums[i + 1]  else 0
            if c == a or c == 0 or a == 0:
                if a == 0:
                    a = c
                continue
            else:
                print(i, a,c)
                return False

        return True
            


print(Solution().isMonotonic([1,1,0]))