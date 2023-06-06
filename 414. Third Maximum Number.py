class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        mynum = list(set(nums))
        if len(mynum) < 3:
            return max(mynum)
        mynum.sort()
        s = mynum[::-1][:3]
        return s[-1]
