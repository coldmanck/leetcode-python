# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion
        '''
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        '''
        
        # iterative soluion with stack (more intuitive!)
        # Time O(2n)=O(n) Space O(n)
        # Reference: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45785/Share-my-two-Python-iterative-solutions-post-order-and-modified-preorder-then-reverse 
        if not root:
            return []
        stack, ans = [(root, False)], []
        while stack:
            root, is_visited = stack.pop()
            if is_visited:
                ans.append(root.val)
            else:
                stack.append((root, True))
                if root.right:
                    stack.append((root.right, False))
                if root.left:
                    stack.append((root.left, False))
        return ans
        
        # iterative soluion with stack (not intuitive!)
        '''
        stack = []
        ans = []
        while stack or root:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            # check if there is a right branch from the current root
            if root.right and stack and (root.right is stack[-1]):
                # If so, replace the root with the right subtree popped out from stack,
                # push the old root back to stack and run another loop starting from the new root
                new_root = stack.pop()
                stack.append(root)
                root = new_root
            else:
                # Else, append the current value to the output array
                ans.append(root.val)
                root = None
        return ans
        '''