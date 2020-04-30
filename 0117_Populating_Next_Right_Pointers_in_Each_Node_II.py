"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # solution 1: level-order queue-based method
        # Time O(n) Space O(n)
        # if not root:
        #     return None
        # level = [root]
        # while level:
        #     for i in range(len(level) - 1):
        #         level[i].next = level[i + 1]
        #     level[-1].next = None
        #     level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        # return root
    
        # solution 2: next-pointer method
        # Time O(n) Space O(1)
        def find_next_node_for_child(node):
            while node:
                if node.left:
                    return node, node.left
                if node.right:
                    return node, node.right
                node = node.next
            return None, None
        
        node = root
        while node:
            node, next_node = find_next_node_for_child(node)
            while node:
                if node.left:
                    node.left.next = node.right if node.right else find_next_node_for_child(node.next)[1]
                if node.right:
                    node.right.next = find_next_node_for_child(node.next)[1]
                node = node.next
            node = next_node
        return root