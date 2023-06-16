class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        index = 1
        for i in sentence.split():
            if i.startswith(searchWord):
                return index
            index +=1
        return -1
