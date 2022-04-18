# Runtime: 32 ms, faster than 54.44% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        if not root:
            return []
        ans, level = [], [root]
        reverse = 0
        while level:
            temp_ans = list(reversed([node.val for node in level])) if reverse else [node.val for node in level]
            reverse ^= 1
            ans.append(temp_ans)
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return ans
        '''
        
        # Runtime: 36 ms, faster than 82.29% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
        # Memory Usage: 14.2 MB, less than 60.22% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
        if not root:
            return []
        queue = [root]
        ans = []
        start_from_left = True
        while queue:
            if start_from_left:
                ans.append([queue[i].val for i in range(len(queue))])
            else:
                ans.append([queue[i].val for i in range(len(queue) - 1, -1, -1)])
            queue = [child for node in queue for child in (node.left, node.right) if child]
            start_from_left = not start_from_left
        return ans