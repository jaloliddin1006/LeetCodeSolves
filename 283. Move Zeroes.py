class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = nums
        for i in nums:
            if i == 0:
                n.remove(0)
                n.append(0)
            else:
                continue
        return n     


print(Solution().moveZeroes([0]))

mylist = [0,1,0,3,12]

print(mylist.remove(0))
print(mylist)