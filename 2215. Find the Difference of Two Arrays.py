class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        index_1 = [i for i, x in enumerate(nums1) if x in nums2]
        index_2 = [i for i, x in enumerate(nums2) if x in nums1]
      
        for i in index_1[::-1]:
            del nums1[i]
        for i in index_2[::-1]:
            del nums2[i]
        return [list(set(nums1)), list(set(nums2))]
    
print(Solution().findDifference([1,2,3,3], [1,1,2,2]))
# ll = [1, 5, 7]
# nums = [1,2,3,1,2,4,5,6,3,2,1]
# print(nums)


# for i in ll[::-1]:
#     del nums[i]
# # nums.pop(1)
# print(nums)

