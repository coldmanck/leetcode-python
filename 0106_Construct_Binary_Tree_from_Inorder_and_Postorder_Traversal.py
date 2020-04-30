# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postorder.reverse() # become mirrored preorder
        inorder = {nb:i for i, nb in enumerate(inorder)}
        def build_tree(post, in_left, in_right):
            if in_left > in_right:
                return None
            root = TreeNode(postorder[post])
            n_right = in_right - inorder[root.val]
            root.right = build_tree(post + 1, inorder[root.val] + 1, in_right)
            root.left = build_tree(post + 1 + n_right, in_left, inorder[root.val] - 1)
            return root
        
        return build_tree(0, 0, len(inorder) - 1)
        