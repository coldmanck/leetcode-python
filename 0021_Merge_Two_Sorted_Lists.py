# Runtime: 40 ms, faster than 23.19% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None: 
            return l1
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        head_orig = head
        
        while l1 or l2:
            if l1 is None:
                head.next = l2
                return head_orig
            if l2 is None:
                head.next = l1
                return head_orig
            if l1.val > l2.val:
                l1, l2 = l2, l1
            head.next = l1
            head = head.next
            l1 = l1.next
        return head_orig