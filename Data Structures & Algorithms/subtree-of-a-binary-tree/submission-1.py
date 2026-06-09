# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        roots = []
        def findSubroot(r):
            if r is None:
                return
            if r.val == subRoot.val:
                roots.append(r)
            findSubroot(r.left)
            findSubroot(r.right)
        
        findSubroot(root)
        if len(roots) == 0:
            return False
        
        def isSame(r, subR):
            if not r and not subR:
                return True
            elif not r or not subR:
                return False
            
            if r.val != subR.val:
                return False
            return isSame(r.left, subR.left) and isSame(r.right, subR.right)

        for r in roots:
            b = isSame(r, subRoot)
            if b:
                return True
        return False
