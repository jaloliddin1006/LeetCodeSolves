class Solution:
    def countBits(self, n: int) -> list[int]:
        ones = []
        for i in range(0, n+1):
            x = i
            binary = ''
            while x > 1:
                binary = str(x % 2) + binary
                x //= 2
            binary = str(x) + binary
            ones.append(binary.count('1'))
        return ones
    
print(Solution().countBits(5))



