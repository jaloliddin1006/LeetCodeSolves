from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        new = []
        nums.sort()
        for x,y,z in zip(nums[::3], nums[1::3], nums[2::3]):
            if abs(x-y) <= k and abs(y-z) <= k and abs(z-x) <= k:
                new.append([x,y,z])
            else:
                return []
        return new