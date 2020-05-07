# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # level-order traversal
        level = [root]
        while level:
            next_level = []
            x_found = y_found = False
            for node in level:
                if node.val == x:
                    x_found = True
                elif node.val == y:
                    y_found = True
                if x_found and y_found:
                    return True
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return False