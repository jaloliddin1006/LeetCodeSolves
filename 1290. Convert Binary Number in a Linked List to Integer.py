class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''
        while head:
            s += str(head.val)
            head = head.next

        return int(s,2)
# print(Solution().getDecimalValue([1,0,1]))


print(int('1001',2))