class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = collections.defaultdict(set)
        colls = collections.defaultdict(set)
        for r in range(3):
            for c in range(3):
                if (matrix[r][c] in rows[r] or matrix[r][c] in colls[c]):
                    return False
                rows[r].add(matrix[r][c]) 
                colls[c].add(matrix[r][c])
        return True 