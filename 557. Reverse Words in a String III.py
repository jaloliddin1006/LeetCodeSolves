class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        s = ""
        for i in a:
            s += i[::-1] + " "


        return s.strip()


print(Solution().reverseWords("Salom Dunyo"))