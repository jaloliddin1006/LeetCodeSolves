class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        l = []
        for i in s:
            if i.isdigit():
                l.append(int(i))
                print(i)
       
        if len(l) != len(set(l)):
            return False
        d = list(l)
        l.sort()
        return  d == l
    

print(Solution().areNumbersAscending("1 box has 3 blue 5 red 6 green and 12 yellow marbles"))