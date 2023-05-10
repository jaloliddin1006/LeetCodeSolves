class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        n = num//3
        nums = [n-1, n, n+1]
        if sum(nums) == num:
          return nums
        return []