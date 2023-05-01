class Solution:
    def countAsterisks(self, s: str) -> int:
        a = s.split("|")
        c = 0
        for i in range(len(a)):
            if i%2 == 0:
                for x in a[i]:
                    if x == "*":
                        c += 1


        return c


print(Solution().countAsterisks("yo|uar|e**|b|e***au|tifu|l"))