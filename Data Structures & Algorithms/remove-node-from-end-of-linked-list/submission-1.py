# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
       
        l = head
        r = head

        for _ in range(n):
            r = r.next
        
        prev = None
        while r:
            prev = l
            l = l.next
            r = r.next

        if not prev:
            return head.next
            
        prev.next = l.next
        return head