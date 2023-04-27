class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False


print(Solution().containsDuplicate([12,123,5,36,75,4,23,645,23,23,33]))