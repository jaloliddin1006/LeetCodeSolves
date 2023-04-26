class Solution:
    def tribonacci(self, n: int) -> int:
        self.n = n
        t = [0, 1, 1]
        if 0<=n<=2:
            return t[n]
        else:
            for i in range(3, n+1):
                t.append(t[i-3]+t[i-2]+t[i-1])
            return t[-1]








a = Solution()
print(a.tribonacci(5))

# out: 7