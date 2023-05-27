# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        height_subroot = height(subRoot)

        def verify_same_tree(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (node1 and not node2) or (node1.val != node2.val):
                return False
            return verify_same_tree(node1.left, node2.left) and verify_same_tree(node1.right, node2.right)
        
        found = False
        def height_main(node):
            if not node:
                return 0
            cur_height = 1 + max(height_main(node.left), height_main(node.right))
            if cur_height == height_subroot:
                if verify_same_tree(node, subRoot):
                    nonlocal found
                    found = True
            return cur_height
        
        height_main(root)
        return found