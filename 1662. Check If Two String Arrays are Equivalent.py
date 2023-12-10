class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        txt1 = "".join(word1)
        txt2 = "".join(word2)
        return txt1 == txt2
        