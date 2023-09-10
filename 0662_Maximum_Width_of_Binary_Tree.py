# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 1
        level = [(root, 0)]
        while level:
            max_width = max(max_width, level[-1][1] - level[0][1] + 1)
            level = [(leaf, k) for node, n in level for (leaf, k) in ((node.left, 2*n+1), (node.right, 2*n+2)) if leaf]
        return max_width