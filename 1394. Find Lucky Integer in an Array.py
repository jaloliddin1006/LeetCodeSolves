class Solution:
    def findLucky(self, arr: list[int]) -> int:
        lucky_num = -1
        my_num = set(arr)
        for i in my_num:
            l = 0
            for j in arr:
                if i == j:
                    l += 1
            if lucky_num < l and i == l :
                lucky_num = l

        return lucky_num


print(Solution().findLucky([2,2, 2,3]))