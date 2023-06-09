class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for i in letters:
            if ord(i) > ord(target):
                return i
        return letters[0]