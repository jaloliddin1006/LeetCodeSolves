class Solution:
    def hammingWeight(self, n: str) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count