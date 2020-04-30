# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # recursion
        '''
        def is_symmetric(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and is_symmetric(node1.left, node2.right) and is_symmetric(node1.right, node2.left)
            
        return is_symmetric(root, root)
        '''
        
        # iterative solution
        if not root:
            return True
        stack = [(root, root)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        return True