class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        num = []
        d=dict()
        for i in nums:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1 
        for i in d:
            if d[i]==1:
                num.append(i)
        return num