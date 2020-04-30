'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def count_uni_trees(root):
            if not root:
                return 0, True
            count_left, left_is_unival = count_uni_trees(root.left)
            count_right, right_is_unival = count_uni_trees(root.right)
            
            count = count_left + count_right
            is_unival = False
            if left_is_unival and right_is_unival:
                if (not root.left and root.right and root.right.val == root.val) or (not root.right and root.left and root.left.val == root.val) or (root.left and root.right and root.left.val == root.val and root.right.val == root.val) or (not root.left and not root.right):
                    count += 1
                    is_unival = True
            return count, is_unival
        
        return count_uni_trees(root)[0]
                
            