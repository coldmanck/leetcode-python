# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if not t1 or not t2:
            t = t1 or t2
            node = TreeNode(val=t.val)
            node.left = self.mergeTrees(t.left, None)
            node.right = self.mergeTrees(t.right, None)
        else:
            node = TreeNode(val=t1.val+t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        return node
        