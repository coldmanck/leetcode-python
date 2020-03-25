# Runtime: 32 ms, faster than 69.94% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13 MB, less than 91.38% of Python3 online submissions for Symmetric Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Run inorder traversal on left subtree and reverse-inorder traversal 
        # on right subtree and check if they equals
        '''Method 1'''
#         inorder_list = []
#         def inorder(node):
#             if node is None:
#                 inorder_list.append(None)
#                 return
#             inorder_list.append(node.val)
#             inorder(node.left)
#             inorder(node.right)
#         inorder(root)
        
#         idx = [0]
#         def inorder_reverse(node):
#             if node is None:
#                 if inorder_list[idx[0]] is None:
#                     idx[0] += 1
#                     return True
#                 return False
#             if node.val != inorder_list[idx[0]]:
#                 return False
#             idx[0] += 1
#             return inorder_reverse(node.right) and inorder_reverse(node.left)
#         return inorder_reverse(root)
        '''Method 2'''
        def is_symmetric(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return node1.val == node2.val and is_symmetric(node1.left, node2.right) and is_symmetric(node1.right, node2.left)
        return is_symmetric(root, root)