class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newList = [""] * ((len(word1)+ len(word2)))
        new = ""
        for i in range(len(newList)):
            if i%2 == 0:
                if word1:
                    newList[i] = word1[0]
                    word1 = word1[1:]
                elif word2:
                    newList[i] = word2[0]
                    word2 = word2[1:]
            elif i%2!=0:
                if word2:
                    newList[i]=word2[0]
                    word2 = word2[1:]
                elif word1:
                    newList[i] = word1[0]
                    word1 = word1[1:]
        for x in newList:
            new += x
            
        return new
    
word1 = "acnm"
word2 = "hjkl"
print( Solution().mergeAlternately("asss", "hj"))

# print( range((len(word1)+ len(word2))))
