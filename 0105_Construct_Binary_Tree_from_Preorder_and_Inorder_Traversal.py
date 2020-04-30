# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder = {nb:i for i, nb in enumerate(inorder)}
        def build_tree(pre, in_left, in_right):
            if in_left > in_right:
                return None
            root = TreeNode(preorder[pre])
            nb_of_left = inorder[root.val] - in_left
            root.left = build_tree(pre + 1, in_left, inorder[root.val] - 1)
            root.right = build_tree(pre + 1 + nb_of_left, inorder[root.val] + 1, in_right)
            return root
        
        return build_tree(0, 0, len(inorder) - 1)