# Runtime: 40 ms, faster than 79.48% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return head
        odd = head
        even_head = even = head.next
        while (odd.next and odd.next.next) or (even.next and even.next.next):
            if odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            if even.next.next:
                even.next = even.next.next
                even = even.next
        odd.next = even_head
        even.next = None
        return head