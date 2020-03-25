# Runtime: 84 ms, faster than 22.95% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 23.1 MB, less than 91.67% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Method 1
        # ans = [None]
        # def lca(node):
        #     if not node:
        #         return False
        #     mid = (node is p or node is q)
        #     left = lca(node.left)
        #     right = lca(node.right)
        #     if mid + left + right >= 2:
        #         ans[0] = node
        #     return mid or left or right
        # lca(root)
        # return ans[0]
        
        # Method 2
        # Time: O(n)
        # Space: O(h)
        if root is None:
            return None
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right