# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        temp1 = list1
        temp2 = list2
        while (temp1 and temp2):
            if temp1.val <= temp2.val:
                cur.next = temp1
                temp1 = temp1.next
            else:
                cur.next = temp2
                temp2 = temp2.next
            cur = cur.next

        while (temp1):
            cur.next = temp1
            temp1 = temp1.next
            cur = cur.next
        while (temp2):
            cur.next = temp2
            temp2 = temp2.next
            cur = cur.next
        return dummy.next
