'''
a few seconds ago	Accepted	44 ms	16.1 MB	python3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        
        return helper(root, float('-inf'), float('inf'))