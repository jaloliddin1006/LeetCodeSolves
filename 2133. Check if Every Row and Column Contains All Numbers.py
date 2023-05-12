import collections
class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        rows = collections.defaultdict(set)
        colls = collections.defaultdict(set)
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if (matrix[r][c] in rows[r] or matrix[r][c] in colls[c]):
                    return False
                rows[r].add(matrix[r][c]) 
                colls[c].add(matrix[r][c])
        return True 