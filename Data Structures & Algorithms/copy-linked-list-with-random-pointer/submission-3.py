"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next
        
        for old, new in oldToNew.items():
            if old.next:
                new.next = oldToNew[old.next]
            if old.random:
                new.random = oldToNew[old.random]
        return oldToNew[head] if head else None
