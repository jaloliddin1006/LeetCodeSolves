class Solution:
    def calPoints(self, operations: list[str]) -> int:
        score = []
        n = 0
        for i in operations:
            
            if i == "D":
                score.append(score[n-1]*2)
                n += 1
                continue
            if i == "C":
                score.pop()
                n -= 1
                continue
            if i == "+":
                score.append(score[n-1]+score[n-2])
                n += 1
                continue
            score.append(int(i))
            n += 1
        return sum(score)
    
    
print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))


# print("-1".isdigit())