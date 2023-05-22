class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        new = t
        for i in s:
            if i in t:
                new = new.replace(i, " ",1)
        return new.strip()
    

print(Solution().findTheDifference('abcd', 'abcde'))