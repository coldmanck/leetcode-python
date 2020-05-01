# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # O(h) time O(1) space iterative solution
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
        
        # O(n) time O(h) space inorder traversal (iteration)
        # find p -> set flag=True once p found -> pick up the next element popped from stack
        '''
        stack = []
        p_found = False
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if p_found:
                return root
            if root is p:
                p_found = True
            root = root.right
        return None
        '''