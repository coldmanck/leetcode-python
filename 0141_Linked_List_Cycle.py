# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # floyd's algorithm (tortoise and hare)
        fast = slow = head
        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False