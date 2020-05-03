# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Time O(n) Space O(h)
        def is_balanced(root): # return (is_balanced, depth)
            if not root:
                return True, 0
            
            left_is_balanced, left_depth = is_balanced(root.left)
            if not left_is_balanced:
                return False, -1
            right_is_balanced, right_depth = is_balanced(root.right)
            if not right_is_balanced:
                return False, -1
            if abs(left_depth - right_depth) > 1:
                return False, -1
            
            depth = max(left_depth, right_depth) + 1
            return True, depth
        
        return is_balanced(root)[0]