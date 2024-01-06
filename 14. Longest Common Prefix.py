class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new = ""
        for i in strs[0]:
            new += i[0]
            for j in strs[1:]:
                if not j.startswith(new):
                    return new[:-1]
            
        return new
        