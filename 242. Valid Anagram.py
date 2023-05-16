class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myset = set(s)
        if len(t) > len(s):
            return False
        for i in myset:
            if s.count(i) > t.count(i):
                return False
        return True