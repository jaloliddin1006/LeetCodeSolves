class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        max_ = arr[0]
        for i in set(arr):
            if arr.count(max_) <= arr.count(i):
                max_ = i

        return max_

        