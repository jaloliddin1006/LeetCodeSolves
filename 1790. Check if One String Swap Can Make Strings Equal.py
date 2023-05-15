class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1.count(s1[i]) != s2.count(s1[i]):

                    return False
                s += 1
            if s == 3:
                return False
        return True
    

print(Solution().areAlmostEqual("banp", "kanb"))