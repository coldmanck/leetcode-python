# Runtime: 80 ms, faster than 16.92% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import math
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def arr2bst(arr, left, right):
            if left > right:
                return None
            mid = math.ceil((left + right)/2)
            node = TreeNode(nums[mid])
            node.left = arr2bst(arr, left, mid - 1)
            node.right = arr2bst(arr, mid + 1, right)
            return node
        return arr2bst(nums, 0, len(nums) - 1)