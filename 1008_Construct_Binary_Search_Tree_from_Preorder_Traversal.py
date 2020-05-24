# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        left, right = 1, len(preorder) - 1
        while left < right:
            mid = (left + right) // 2
            if preorder[mid] < root.val:
                left = mid + 1
            else:
                right = mid
        if preorder[left] < root.val:
            root.left = self.bstFromPreorder(preorder[1:])
        else:
            root.right = self.bstFromPreorder(preorder[left:])
            root.left = self.bstFromPreorder(preorder[1:left])
        return root