class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        negatives = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                elem = grid[i][j]
                if elem >= 0:
                    continue
                negatives += len(grid[0]) - j
                break

        return negatives
    
    
    
    