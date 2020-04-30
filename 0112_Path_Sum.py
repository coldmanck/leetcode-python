# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # iterations
        if not root:
            return False
        cur_sum = 0
        stack = [(root, cur_sum)]
        while stack:
            root, cur_sum = stack.pop()
            if not root:
                continue
            cur_sum += root.val
            if not root.left and not root.right:
                if cur_sum == sum:
                    return True
                else:
                    continue
            stack.append((root.left, cur_sum))
            stack.append((root.right, cur_sum))
        return False
            
        
        # my recursion solution
        '''
        def has_path_sum(root, sum, cur_sum):
            cur_sum += root.val
            if not root.left and not root.right and sum == cur_sum:
                return True
            left = has_path_sum(root.left, sum, cur_sum) if root.left else False
            right = has_path_sum(root.right, sum, cur_sum) if root.right else False
            return left or right
        
        if not root:
            return False
        return has_path_sum(root, sum, 0)
        '''

        # cleaner recursion solution
        '''
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        '''