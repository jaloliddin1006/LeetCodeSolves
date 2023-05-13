class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        large = 0
        for i in accounts:
            s = 0
            # print(i)
            for j in i:
                # print(i,j)
                s += j
            large = max(large, s)
        return large
    

print(Solution().maximumWealth( [[1,5],[7,3],[3,5]]))