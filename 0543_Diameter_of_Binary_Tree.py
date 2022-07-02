# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''With a follow-up that reuqires to print the path of the (longest) diameter'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
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
            # maximum_diameter[0] = max(maximum_diameter[0], max_node_diameter)
            if max_left_path_len > max_right_path_len:
                return 1 + max_left_path_len, left_path + [node]
            else:
                return 1 + max_right_path_len, right_path + [node]
            # return 1 + max(max_left_path_len, max_right_path_len)
        
        helper(root)
        print([i.val for i in maximum_diameter[1]])
        return maximum_diameter[0]