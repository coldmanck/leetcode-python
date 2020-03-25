# Runtime: 40 ms, faster than 18.21% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 18.8 MB, less than 20.45% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''Iterative solution'''
        # prev = None
        # curr = head
        # while curr:
        #     nextt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextt
        # return prev
        
        '''Recursive solution'''
        def reverse_helper(node):
            if node is None or node.next is None:
                return node
            # reverse_helper(node.next).next = head
            p = reverse_helper(node.next)
            node.next.next = node
            node.next = None
            return p
        return reverse_helper(head)
        
        