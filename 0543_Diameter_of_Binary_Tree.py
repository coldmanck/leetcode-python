# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''With a follow-up that reuqires to print the path of the (longest) diameter'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Way 1: use array to store or use the nonlocal keyword
        ans = 1 # [1]

        def helper(node):
            if not node:
                return 0
            left_depth, right_depth = helper(node.left), helper(node.right)
            max_len = 1 + left_depth + right_depth
            
            nonlocal ans 
            ans = max(ans, max_len) # ans[0] = max(ans[0], max_len)
            
            return 1 + max(left_depth, right_depth)
        
        helper(root)
        return ans - 1 # ans[0] - 1

        # Way 2
        '''
        maximum_diameter = [0, [root]]
        
        def helper(node):
            if not node:
                return 0, []
            max_left_path_len, left_path = helper(node.left)
            max_right_path_len, right_path = helper(node.right)
            max_node_diameter = max_left_path_len + max_right_path_len
            if max_node_diameter > maximum_diameter[0]:
                maximum_diameter[0] = max_node_diameter
                maximum_diameter[1] = left_path + [node] + right_path
            if max_left_path_len > max_right_path_len:
                return 1 + max_left_path_len, left_path + [node]
            else:
                return 1 + max_right_path_len, right_path + [node]
        
        helper(root)
        print([i.val for i in maximum_diameter[1]])
        return maximum_diameter[0]
        '''