# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion
        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        # iterative solution with a stack
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return ans