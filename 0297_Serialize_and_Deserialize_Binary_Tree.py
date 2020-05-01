# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder_traversal(root):
            if not root:
                return 'None'
            return ','.join([str(root.val), preorder_traversal(root.left), preorder_traversal(root.right)])
    
        return preorder_traversal(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # DFS + queue: Time O(n) Space O(n)
        from collections import deque
        data = deque(data.split(','))
        def build_tree_from_inorder(data):
            node = data.popleft()
            if node == 'None':
                return None
            root = TreeNode(str(node))
            root.left = build_tree_from_inorder(data)
            root.right = build_tree_from_inorder(data)
            return root
        
        return build_tree_from_inorder(data)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))