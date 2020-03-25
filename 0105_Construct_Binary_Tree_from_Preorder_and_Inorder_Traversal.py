# Runtime: 60 ms, faster than 80.10% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 17.8 MB, less than 86.84% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        i_dict = {str(inorder[i]): i for i in range(len(inorder))}
        
        def build_tree(in_left, in_right, pre_idx):
            if in_left > in_right:
                return None
            val = preorder[pre_idx]
            in_idx = i_dict[str(val)]
            root = TreeNode(val)
            left_mid = pre_idx + 1
            if 0 <= left_mid < len(preorder):
                root.left = build_tree(in_left, in_idx - 1, left_mid)
            right_mid = pre_idx + 1 + (in_idx - in_left)
            if 0 <= right_mid < len(preorder):
                root.right = build_tree(in_idx + 1, in_right, right_mid)
            return root
        
        return build_tree(0, len(inorder)-1, 0)