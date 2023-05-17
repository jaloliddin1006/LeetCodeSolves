class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        mycor= 1000000
        ind = -1
        for cor in points:
            if x==cor[0] or y==cor[1] :
                man = abs(x-cor[0])+abs(y-cor[1])
                if man < mycor:
                    mycor = man
                    ind = points.index(cor)
           
        return ind
    


print(Solution().nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))

   