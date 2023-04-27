class Solution:
    def addBinary(self, a: str, b: str) -> str:
        self.a = a
        self.b = b

        s = int(a,2) + int(b,2)
        return str(bin(s))[2:]



print(Solution().addBinary("10", "11"))

#out: 101