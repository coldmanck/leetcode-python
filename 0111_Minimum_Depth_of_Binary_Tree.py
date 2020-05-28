# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        min_depth = 1
        if root.left and not root.right:
            min_depth += self.minDepth(root.left)
        elif root.right and not root.left:
            min_depth += self.minDepth(root.right)
        elif root.left and root.right:
            min_depth += min(self.minDepth(root.left), self.minDepth(root.right))
        return min_depth