class Solution:
    def climbStairs(self, n: int) -> int:
        mylist = [1, 2]
        if n==1:
            return 1
        else:
            for i in range(2, n):
                mylist.append(mylist[i-2] + mylist[i-1])
            return mylist[-1]
    



print(Solution().climbStairs(2))

    # 4
    # 1 1 1 1
    # 2 1 1
    # 1 2 1
    # 1 1 2
    # 2 2

    # 2>2 #
    # 3>3 #+1
    # 4>5 # +2
    # 5>8 # +3
    # 6>13 # +5
    # 7>21 # +8
    # 8>34 # +13
