# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not self.pruneTree(root.left):
            root.left = None
        if not self.pruneTree(root.right):
            root.right = None
        if root.left or root.right or root.val == 1:
            return root
        return None