# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''All time, space complexity are O(N) where N is the number of nodes in the BST'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Inorder DFS: 88 ms	16.2 MB	python3
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
        
        # Iterative BFS: 84 ms	16.1 MB	python3
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
        
        # Iterative DFS: 72 ms	16.3 MB	python3
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
        
        # Recursion: 44 ms	16.1 MB	python3
        '''
        def helper(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        
        return helper(root, float('-inf'), float('inf'))
        '''