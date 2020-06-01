# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # recursion: Time O(n) Space O(h)
        # if not root:
        #     return None
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root
    
        # iterative solution: Time O(n) Space O(h)
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.extend([node.left, node.right])
        return root