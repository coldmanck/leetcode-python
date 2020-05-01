# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Recursion (Preorder DFS)
        def helper(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        
        return helper(root, float('-inf'), float('inf'))
        
        # Recursion (Inorder DFS)
        '''
        def helper(node, prev_val):
            if not node:
                return True, prev_val
            # check left subtree
            is_valid, prev_val = helper(node.left, prev_val)
            if not is_valid:
                return False, prev_val
            # check current node
            if prev_val >= node.val:
                return False, prev_val
            prev_val = node.val
            # check right subtree
            is_valid, prev_val = helper(node.right, prev_val)
            if not is_valid:
                return False, prev_val
            
            return True, prev_val
        return helper(root, float('-inf'))[0]
        '''
    
        # Iteration (Preorder DFS)
        '''
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            if not lower < root.val < upper:
                return False
            stack.append([root.left, lower, root.val])
            stack.append([root.right, root.val, upper])
        return True
        '''
        
        # Iteration (Inorder DFS)
        '''
        if not root:
            return True
        stack = []
        last_node_val = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.val > last_node_val:
                return False
            last_node_val = root.val
            root = root.right
        return True
        '''
        
        # Iteration BFS
        '''
        from collections import deque
        if not root:
            return True
        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            root, lower, upper = queue.popleft()
            if not root:
                continue
            if not lower < root.val < upper:
                return False
            queue.append((root.left, lower, root.val))
            queue.append((root.right, root.val, upper))
        return True
        '''
        
        