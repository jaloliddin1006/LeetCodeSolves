class Solution:
    def getLucky(self, s: str, k: int) -> int:
        self.s = s
        self.k = k

        alpha = "abcdefghijklmnopqrstuvwxyz"
        s_num = [lambda arg=x: alpha.index(arg)+1 for x in s]
        my_list = ''
        for n in s_num:
                my_list += str(n())
        for i in range(k):
            b = 0
            for i in str(my_list):
                 b += int(i)
            my_list = b
            
            
        return my_list




a = Solution()
print(a.getLucky('iiii',1))