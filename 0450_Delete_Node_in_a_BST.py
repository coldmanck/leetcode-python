# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time O(h) Space O(h)
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key == root.val:
            if not root.left and not root.right: # if is a leaf simply delete it
                return None
            if (root.left and not root.right) or (root.right and not root.left): # if has only 1 child -> replace with the child
                return root.left or root.right
            # if has two children -> use either replace with sucessor (the choice here) or predecessor
            prev, node = root, root.right
            is_left = False
            while node.left:
                is_left = True
                prev, node = node, node.left
            if is_left:
                prev.left = node.right
            else:
                prev.right = node.right
            # remember to reconnect all connections
            node.left = root.left
            node.right = root.right
            return node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root