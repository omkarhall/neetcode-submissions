# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        skip = True
        fast = head
        slow = head
        while fast and slow:
            if fast == slow and not skip:
                return True
            if skip:
                skip = False
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return False