class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        s = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                s.append("FizzBuzz")
                continue
            elif i % 5 == 0:
                s.append("Buzz")
                continue
            elif i % 3 == 0:
                s.append("Fizz")
                continue
            else:
                s.append(f"{i}")


        return s


print(Solution().fizzBuzz(5))