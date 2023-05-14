class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        mylist = []
        nums = s.split(":")
        for i in range(ord(nums[0][0]), ord(nums[1][0])+1):
            for j in range(int(nums[0][1]), int(nums[1][1])+1 ):
                mylist.append(f"{chr(i)}{j}")
        return mylist
        

print(Solution().cellsInRange("A1:D3"))