class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        large = [0, 0]
        for i in range(len(mat)):
            ones = mat[i].count(1)
            if large[1] < ones:
                large[0] = i
                large[1] = ones
        return large
