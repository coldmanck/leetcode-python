# Runtime: 68 ms, faster than 76.78% of Python3 online submissions for Delete Nodes And Return Forest.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Delete Nodes And Return Forest.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def del_nodes(root):
            if not root:
                return None
            if root.val in to_delete:
                left = del_nodes(root.left)
                if left:
                    ans.append(left)
                right = del_nodes(root.right)
                if right:
                    ans.append(right)
                return None
            else:
                root.left = del_nodes(root.left)
                root.right = del_nodes(root.right)
                return root
        
        to_delete = set(to_delete)
        ans = [] if root.val in to_delete else [root]
        del_nodes(root)
        return ans