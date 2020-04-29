# Runtime: 32 ms, faster than 23.58% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
        # iterative with stack
        ans = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
                