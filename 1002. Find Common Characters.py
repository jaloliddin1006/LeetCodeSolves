class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        my = []
        other = words[1:]
        for i in words[0]:
            new = i
            for j in range( len(other)):
                if i not in other[j]:
                    new = None
                    break
                else:
                    other[j] = other[j].replace(i, "", 1)
            my.append(new)
        return [x for x in my if x is not None]

