class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = []
        cols = []
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    rows.append(r)
                    cols.append(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in rows or c in cols:
                    matrix[r][c] = 0
        return matrix
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeroes(matrix))
      