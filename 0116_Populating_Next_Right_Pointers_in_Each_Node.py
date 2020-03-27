# Runtime: 72 ms, faster than 20.24% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.4 MB, less than 35.71% of Python3 online submissions for Populating Next Right Pointers in Each Node.

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
        if not root:
            return None
        level = [root]
        while level:
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
            level[-1].next = None
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return root