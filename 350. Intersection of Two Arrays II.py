class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a = []
        for i in nums1:
            if i in nums2:  
                a.append(i)
                nums2.remove(i)
        return a

print(Solution().intersect([1,2,2,3], [1,1,2,2]))
