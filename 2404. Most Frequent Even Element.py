class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        large_len = 0
        even_nums = []
        for i in set(nums):
            if i%2 == 0:
                print(even_nums)
                if nums.count(i) > large_len: 
                    even_nums = [i]
                    large_len = nums.count(i)
                    continue
                if nums.count(i) == large_len:
                    even_nums.append(i)
                    continue
            
        return min(even_nums) if even_nums else -1
mylist = [4,4,4,9,2,4]
print(Solution().mostFrequentEven(mylist))