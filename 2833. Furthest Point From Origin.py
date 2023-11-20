class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r = moves.count("R")
        l = moves.count("L")
        pref = moves.count("_")
        res = r-l if r>l else l-r
        return res + pref
        