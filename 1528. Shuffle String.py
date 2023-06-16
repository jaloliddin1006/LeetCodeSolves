class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = set()
        for i in range(len(indices)):
            a.add((indices[i],s[i]))
        s = ""
        for i in sorted(a):
            s += i[1]
        return s