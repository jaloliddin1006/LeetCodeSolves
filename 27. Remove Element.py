class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        self.nums = nums
        self.val = val
        while True:
            try:
                a = nums.index(val)
            except: break
            nums.pop(a)
        return len(nums)