from nums import my_list
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        long_seq = 0
        my_num = set(nums)
        for i in my_num:
            curr = 1
            n = i
            if i - 1 in my_num:
                continue
            while n + 1 in my_num:
                curr += 1
                n += 1
            long_seq = max(long_seq, curr)
        return long_seq


print(Solution().longestConsecutive([100,4,200,1,3,2,199,201,99,200]))