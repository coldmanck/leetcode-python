# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        '''Recursive searching (~= DFS)
        Time: O(h), avg O(logn) worst O(n)
        Space: O(h), avg O(logn) worst O(n)
        Runtime: 80 ms, faster than 39.16% of Python3 online submissions for Search in a Binary Search Tree.
        Memory Usage: 15.6 MB, less than 9.09% of Python3 online submissions for Search in a Binary Search Tree.
        '''
        # if not root or root.val == val:
        #     return root
        # return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
        
        '''Iterative searching
        Time: O(h), avg O(logn) worst O(n)
        Space: O(1)
        Runtime: 84 ms, faster than 18.89% of Python3 online submissions for Search in a Binary Search Tree.
        Memory Usage: 15.8 MB, less than 9.09% of Python3 online submissions for Search in a Binary Search Tree.
        '''
        while root:
            if root.val == val:
                return root
            root = root.left if val < root.val else root.right
        return None