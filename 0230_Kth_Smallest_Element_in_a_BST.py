# Runtime: 48 ms, faster than 78.09% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 17.5 MB, less than 7.27% of Python3 online submissions for Kth Smallest Element in a BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''(recursive) inorder traversal to the k-th element'''
#         nb = [0]
#         def inorder(node, nb):
#             if not node:
#                 return None
#             val = inorder(node.left, nb)
#             if val is not None:
#                 return val
            
#             nb[0] += 1
#             if nb[0] == k:
#                 return node.val
            
#             val = inorder(node.right, nb)
#             if val is not None:
#                 return val
#         return inorder(root, nb)
        '''(iterative) inorder traversal to the k-th element'''
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right