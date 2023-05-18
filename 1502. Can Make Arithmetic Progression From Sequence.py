class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        print(arr)
        for i in range(len(arr)-2):
            print(i)
            if abs(arr[i+1]-arr[i]) == abs(arr[i+2]-arr[i+1]):
                continue
            else:
                return False
        return True
    

print(Solution().canMakeArithmeticProgression([3,5,1,-1]))