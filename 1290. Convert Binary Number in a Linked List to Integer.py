class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return head.val
    

# print(Solution().getDecimalValue([1,0,1]))


print(int('1001',2))