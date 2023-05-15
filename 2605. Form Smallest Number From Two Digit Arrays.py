class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        for i in nums1:
            if i in nums2:
                return i
        min1 = min(nums1)
        min2 = min(nums2)
        return int(f"{min(min1, min2)}{max(min1, min2)}")