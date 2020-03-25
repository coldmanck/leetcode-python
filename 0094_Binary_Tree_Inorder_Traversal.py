# Runtime: 32 ms, faster than 23.58% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''Method 1: recursive'''
        # def inorder(root, ans):
        #     if root is None:
        #         return
        #     inorder(root.left, ans)
        #     ans.append(root.val)
        #     inorder(root.right, ans)
        # ans = []
        # inorder(root, ans)
        # return ans
        '''Method 2: iterative using stack'''
        stack = []
        ans = []
        node = root
        while stack or node:
            # add nodes to the left into stack
            while node:
                stack.append(node)
                node = node.left
            # pop a element and add into the answer list
            node = stack.pop()
            ans.append(node.val)
            # perform the same procedure at the right subtree
            node = node.right
        return ans
                
            
        
                