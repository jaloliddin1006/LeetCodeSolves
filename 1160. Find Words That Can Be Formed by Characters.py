class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = ''
        for word in words:
            w = ''
            for i in word:
                if word.count(i) > chars.count(i):
                   w = ''
                   break
                w += i
            s += w
        return len(s)