# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        # compute length
        end = head
        length = 1
        while end.next:
            length += 1
            end = end.next
        
        if k == length:     # if k equals length -> no need to rotate -> return
            return head
        elif k > length:    # if k > length -> take only the remainder
            k %= length

        end.next = head
        idx = 0
        while idx != length - k - 1:
            idx += 1
            head = head.next
        new_head = head.next
        head.next = None
        
        return new_head