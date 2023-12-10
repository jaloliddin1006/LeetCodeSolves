class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new = []
        w = len(matrix[0])
        h = len(matrix)
        for i in range(w):
            row = []
            for j in range(h):
                row.append(matrix[j][i])
            new.append(row)
        return new
