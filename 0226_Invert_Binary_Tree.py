# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # recursion: Time O(n) Space O(h)
        # def invert_tree(root):
        #     if not root:
        #         return None
        #     left = invert_tree(root.left)
        #     right = invert_tree(root.right)
        #     root.right = left
        #     root.left = right
        #     return root
        # return invert_tree(root)
    
        # iterative solution: Time O(n) Space O(h)
        if not root:
            return None
        head = root
        stack = [root]
        while stack:
            root = stack.pop()
            root.right, root.left = root.left, root.right
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return head