class Solution:
    def longestPalindrome(self, s: str) -> int:
        # if len(s)==2 and s[0] == s[1]:
        #     return 2
        if len(s)==2 and s[0] != s[1]:
            return 1
        letters = set(x for x in s)
        if len(letters) == 1:
            return len(s)
        print(letters)
        l = len(s)
        for i in letters:
            if s.count(i) % 2 != 0:
                print(i)
                l -= 1


        return l
    

print(Solution().longestPalindrome("asadfd"))