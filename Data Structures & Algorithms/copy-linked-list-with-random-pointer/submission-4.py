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
            new.next = oldToNew.get(old.next, None)
            new.random = oldToNew.get(old.random, None)
        return oldToNew.get(head, None)
