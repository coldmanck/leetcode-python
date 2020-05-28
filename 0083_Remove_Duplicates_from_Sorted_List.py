# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev, curr = head, head.next
        while curr:
            if curr.val == prev.val:
                while curr and curr.val == prev.val:
                    curr = curr.next
                prev.next = curr
            else:
                prev, curr = curr, curr.next
        return head