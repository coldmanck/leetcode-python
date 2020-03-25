# Runtime: 44 ms, faster than 31.86% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15 MB, less than 90.62% of Python3 online submissions for Maximum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''DFS Method 1'''
        # def dfs(node, depth):
        #     if node is None:
        #         return depth
        #     depth += 1
        #     d1 = dfs(node.left, depth)
        #     d2 = dfs(node.right, depth)
        #     return max(d1, d2)
        # return dfs(root, 0)
    
        '''DFS Method 2'''
        # ans = [0]
        # def dfs(node, depth):
        #     if node is not None:
        #         depth += 1
        #         ans[0] = depth if ans[0] < depth else ans[0]
        #         dfs(node.left, depth)
        #         dfs(node.right, depth)
        # dfs(root, 0)
        # return ans[0]
        
        '''DFS Method 3'''
        def dfs(node):
            if node is None:
                return 0
            d1 = dfs(node.left)
            d2 = dfs(node.right)
            return 1 + max(d1, d2)
        return dfs(root)