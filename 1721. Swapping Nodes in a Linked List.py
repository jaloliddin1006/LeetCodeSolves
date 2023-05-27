# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        while head:
            a.append(head.val)
            head = head.next

        b = a[k - 1]
        c = a[-k]

        a[k - 1] = c
        a[-k] = b

        new_head = ListNode(a[0])
        curr = new_head

        for i in range(1, len(a)):
            curr.next = ListNode(a[i])
            curr = curr.next

        return new_head