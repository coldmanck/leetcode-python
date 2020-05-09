# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        is_circle = False
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                is_circle = True
                break
        if not is_circle:
            return None
        fast = head
        while fast and slow and fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast