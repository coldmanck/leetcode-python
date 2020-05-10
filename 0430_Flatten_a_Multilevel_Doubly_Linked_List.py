# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flat(node):
            if not node: # case 1: node is None
                return None
            if not node.child: # case 2 & 3: node.child is None
                if node.next:
                    return flat(node.next) 
                else: 
                    return node
            # case 4 & 5: node.child is not None
            child_tail = flat(node.child)
            child_tail.next = node.next
            node.next = node.child
            node.next.prev = node
            node.child = None
            if child_tail.next: # case 4: node.next is not None
                child_tail.next.prev = child_tail
                return flat(child_tail.next)
            return child_tail # case 5: node.next is None
        
        flat(head)
        return head