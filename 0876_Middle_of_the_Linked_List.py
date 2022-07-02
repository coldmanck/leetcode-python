# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        # while fast.next:
        #     fast = fast.next
        #     if fast.next:
        #         fast = fast.next
        #     slow = slow.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow