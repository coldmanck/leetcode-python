# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # Iteration (1): Time O(h) Space O(1)
        if not root:
            return TreeNode(val)
        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
        return root
    
        # Iteration (2): Time O(h) Space O(1)
        '''
        if not root:
            return TreeNode(val)
        
        node = root
        succ = root.left if val < root.val else root.right
        while succ:
            node = succ
            succ = succ.left if val < succ.val else succ.right
        if val < node.val:
            node.left = TreeNode(val)
        else:
            node.right = TreeNode(val)
        return root
        '''
        
        # Recursion (1): Time O(h) Space O(h)
        '''
        def insert_node(root, val):
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                else:
                    insert_node(root.left, val)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                else:
                    insert_node(root.right, val)
        
        if not root:
            return TreeNode(val)
        insert_node(root, val)
        return root
        '''
        
        # Recursion (2): Time O(h) Space O(h)
        '''
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
        '''