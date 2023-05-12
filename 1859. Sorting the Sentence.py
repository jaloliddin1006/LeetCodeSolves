import collections
class Solution:
    def sortSentence(self, s: str) -> str:
        sorted_text = collections.defaultdict()
        text = s.split(" ")
        for i in text:
            sorted_text[int(i[-1])] = i[:-1]
        
        a = dict(sorted(sorted_text.items()))
        b = ""
        for j in a:
            b += a[j] + " "

        return b.strip()








print(Solution().sortSentence("is2 sentence4 This1 a3"))