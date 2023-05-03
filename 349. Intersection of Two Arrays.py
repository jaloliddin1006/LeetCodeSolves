class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        index_1 = [i for i, x in enumerate(nums1) if x in nums2]
        num_1 = []
        for i in index_1[::-1]:
            num_1.append(nums1[i])
        return list(set(num_1))
    
print(Solution().intersection([1,2,3,3], [1,1,2,2]))