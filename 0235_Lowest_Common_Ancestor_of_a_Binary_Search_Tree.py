# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''Method 1: applies to only BST'''
        # Time O(h) Space O(h)
        # if not root:
        #     return None
        # if root is p or root is q: # actually this is not needed here
        #     return root
        # if p.val < root.val and q.val < root.val: # ~= if left is not None
        #     return self.lowestCommonAncestor(root.left, p, q)
        # if p.val > root.val and q.val > root.val: # ~= if right is not None
        #     return self.lowestCommonAncestor(root.right, p, q)
        # return root # ~= if left and right

        '''Method 2: Iterative Method 1'''
        # Time O(h) Space O(1)
        if not root:
            return None
        stack = [root]
        while stack:
            root = stack.pop()
            if not root: # actually this is not needed here
                continue
            if root is p or root is q: # actually this is not needed here
                return root
            if p.val < root.val and q.val < root.val: # ~= if left is not None
                stack.append(root.left)
            elif p.val > root.val and q.val > root.val: # ~= if right is not None
                stack.append(root.right)
            else:
                return root
        return None

        '''Method 3: applies to both BST/Binary Tree'''
        # Time O(h) Space O(h)
        # if not root:
        #     return None
        # if root is p or root is q:
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right:
        #     return root
        # else:
        #     return left or right