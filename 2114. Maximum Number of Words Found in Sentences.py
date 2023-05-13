class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        large = 0
        for gap in sentences:
            text = gap.split(" ")
            large = max(large, len(text))

        return large