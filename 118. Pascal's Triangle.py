class Solution:
    def generate(self, numRows: int):
        self.numRows = numRows

        triangle = [[1], [1,1]]
        if numRows == 1:
            return [triangle[0]]
        elif numRows == 2:
            return triangle
        else:
            for i in range(1, numRows-1):
                tri = triangle[i]
                row = []
                row.append(1)
                for x in range(len(tri)-1):
                    row.append(tri[x]+tri[x+1])
                row.append(1)
                triangle.append(row)
              
        return triangle

a = Solution()

print(a.generate(2))

