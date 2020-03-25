# Runtime: 36 ms, faster than 38.12% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''BFS with queue method'''
        # ans = []
        # temp_ans = []
        # queue = deque()
        # queue.append((root, 0))
        # old_level = 0
        # if root is None:
        #     return []
        # while queue:
        #     root, level = queue.popleft()
        #     if old_level != level:
        #         ans.append(temp_ans)
        #         old_level = level
        #         temp_ans = []
        #     temp_ans += [root.val]
        #     if root.left:
        #         queue.append((root.left, level + 1))
        #     if root.right:
        #         queue.append((root.right, level + 1))
        # if temp_ans:
        #     ans.append(temp_ans)
        # return ans
        '''Method 2'''
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return ans