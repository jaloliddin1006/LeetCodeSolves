class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = moves.lower()
        r = moves.count("r")
        l = moves.count("l")
        u = moves.count("u")
        d = moves.count("d")

        if r==l and u==d:
            return True
        return False