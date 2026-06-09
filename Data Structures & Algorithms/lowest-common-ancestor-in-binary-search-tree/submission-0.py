# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findPath(self, root, path, x):
            if not root:
                return False
            
            path.append(root)
            
            if root.val == x:
                return True
            
            if self.findPath(root.left, path, x) or self.findPath(root.right, path, x):
                return True
            
            path.pop()
            return False
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1, path2 = [], []

        self.findPath(root, path1, p.val)
        self.findPath(root, path2, q.val)
        print(len(path1))
        for i in range (min(len(path1), len(path2)) - 1, -1, -1):
            if path1[i] == path2[i]:
                return path1[i]
        return root