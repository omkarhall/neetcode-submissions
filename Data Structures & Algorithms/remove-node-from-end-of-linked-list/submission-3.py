# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for i in range(0,n-1):
            first = first.next
        
        cur = head
        prev = None
        while first.next:
            first = first.next
            prev = cur
            cur = cur.next
        
        if not prev:
            return head.next
        elif prev.next and prev.next.next:
            prev.next = prev.next.next
        elif prev.next and not prev.next.next:
            prev.next = None
        else:
            return None
        return head