# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        tailNode = ListNode(head.val)
        cur = head.next
        while (cur is not None):
            newNode = ListNode(cur.val, next = tailNode)
            tailNode = newNode
            cur = cur.next

        return newNode