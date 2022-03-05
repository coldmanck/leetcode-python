"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serialized = []
        def preorder(node):
            if not node:
                return
            serialized.append(str(node.val))
            for child in node.children:
                preorder(child)
            serialized.append('#')
        preorder(root)
        return ' '.join(serialized)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        tokens = deque(data.split())
        if len(tokens) == 0:
            return None
        
        root = Node(int(tokens.popleft()), [])
        def helper(node):
            if len(tokens) == 0:
                return
            while tokens[0] != '#':
                child = Node(int(tokens.popleft()), [])
                node.children.append(child)
                helper(child)
            tokens.popleft()
            return root
        return helper(root)