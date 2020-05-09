# Runtime: 32 ms, faster than 65.17% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # keep the n-th and the (n+1)-th node when traversing
        dist_count = 0 # count until n+1
        node = head
        prev = None
        while node:
            node = node.next
            dist_count += 1
            if dist_count == n + 1:
                prev = head
            elif dist_count > n + 1:
                prev = prev.next
        if prev:
            to_del = prev.next
            prev.next = prev.next.next
            del to_del
        elif dist_count == n: # remember the case where dist_count equals n! need to delete the head!
            new_head = head.next
            del head
            head = new_head
        return head
                