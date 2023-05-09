class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        len_mat = len(mat)
        for r in range(len_mat):
            for c in range(len_mat):
                if r == c:
                    s += mat[r][c]
                    s += mat[r][len_mat-c-1]
        if len_mat % 2 == 0:
            return s
        return s-mat[len_mat//2][len_mat//2]