class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        index = word.index(ch)
        reverse = ""
        cont = word[index+1:]

        for i in word:
            if i == ch:
                reverse = i + reverse

                break
            reverse = i + reverse
        return reverse + cont
    


print(Solution().reversePrefix("absdopll", "o"))
