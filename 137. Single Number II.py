# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         d=dict()
#         for i in nums:
#             if i not in d:
#                 d[i]=1 
#             else:
#                 d[i]+=1 
#         for i in d:
#             if d[i]==1:
#                 return i 

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        my_nums = set(nums)
        while my_nums:
            num = my_nums.pop()
            count_ = 0
            for i in nums:
                if num == i:
                    count_ += 1
                if count_ > 1:
                    break
            if count_ == 1:
                return num

print(Solution().singleNumber([2,2,3,2, 1, 3]))

# def IterNext(s):
#     return next(iter(s))
# def PopAdd(s):
#     e = s.pop()
#     return e
# a = {1}
# print(PopAdd(a))
# if a:
#     print(PopAdd(a))