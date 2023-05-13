# #medium

# class Solution:
#     def mostPoints(self, questions: list[list[int]]) -> int:
#         large = 0
#         for q in range(len(questions)):
#             print("  ###  ", q, "  ###")
#             s = 0
#             n = 0
#             l = 0
#             for i in questions[q:]:
#                 if n == l:
#                     l = i[1]
#                     s += i[0]
#                     n = 0
#                 else:
#                     n += 1
#                 print(s)
#             large = max(large, s)
#             print("------")
#         print("--++++++++++++----")
#         return large
    


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        print(dp)
        for i in range(n - 1, -1, -1):
            p, b = questions[i]
            # print(p,b)
            if i + b + 1 < n:
                dp[i] = max(p + dp[i + b + 1], dp[i + 1])
                print(p + dp[i + b + 1], dp[i + 1])
            else:
                dp[i] = max(p, dp[i + 1])
                print(p, dp[i + 1])
        print(dp)

        return dp[0]
    


questions = [[21,5],[35,5],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]
#              0       1      2      3      4     5      6      7
print(Solution().mostPoints(questions))


