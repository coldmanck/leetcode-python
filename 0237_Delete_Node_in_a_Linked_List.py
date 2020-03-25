# Runtime: 44 ms, faster than 8.82% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Delete Node in a Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
                break