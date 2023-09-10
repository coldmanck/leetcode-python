# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def helper(node, cur_sum, cur_path):
            if not node.left and not node.right and cur_sum == 0:
                ans.append(cur_path[:])
                return
            if node.left:
                helper(node.left, cur_sum - node.left.val, cur_path + [node.left.val])
            if node.right:
                helper(node.right, cur_sum - node.right.val, cur_path + [node.right.val])
        helper(root, targetSum - root.val, [root.val])
        return ans

        # if not root:
        #     return []
        # ans = []
        # def helper(node, cur_sum, cur_path):
        #     if not node:
        #         return
        #     cur_sum -= node.val
        #     cur_path.append(node.val)
        #     if not node.left and not node.right and cur_sum == 0:
        #         ans.append(list(cur_path))
        #     helper(node.left, cur_sum, cur_path)
        #     helper(node.right, cur_sum, cur_path)
        #     cur_path.pop()
        # helper(root, targetSum, [])
        # return ans