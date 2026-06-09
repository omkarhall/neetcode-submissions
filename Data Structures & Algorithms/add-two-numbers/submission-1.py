# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = temp = ListNode()
        while cur1 and cur2:
            val = cur1.val + cur2.val + carry
            if val >= 10:
                carry = val // 10
            else:
                carry = 0
            temp.next = ListNode(val % 10)
            temp = temp.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1:
            val = cur1.val + carry
            if val >= 10:
                carry = val // 10
            else:
                carry = 0
            temp.next = ListNode(val % 10)
            temp = temp.next
            cur1 = cur1.next
        
        while cur2:
            val = cur2.val + carry
            if val >= 10:
                carry = val // 10
            else:
                carry = 0
            temp.next = ListNode(val % 10)
            temp = temp.next
            cur2 = cur2.next
        
        if carry > 0:
            temp.next = ListNode(carry)
        return dummy.next