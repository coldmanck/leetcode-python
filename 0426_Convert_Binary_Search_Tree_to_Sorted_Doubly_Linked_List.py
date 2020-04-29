# Runtime: 36 ms, faster than 55.87% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
# Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''Time O(n) Space O(h)'''
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def tree_to_doubly_list(root):
            if not root:
                return None, None
            
            left_tail, left_head = tree_to_doubly_list(root.left)
            # left_tail is used to connect with lower elements
            if left_tail:
                left_tail.right = root
                root.left = left_tail
            
            right_tail, right_head = tree_to_doubly_list(root.right)
            # right_head is used to connect with upper elements
            if right_head:
                right_head.left = root
                root.right = right_head
            
            # left_head and right_tail are kept as the final head and tail
            return (right_tail or root, left_head or root)
        
        if not root:
            return None
        tail, head = tree_to_doubly_list(root)
        tail.right = head
        head.left = tail
        return head