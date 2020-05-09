# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(n) time O(1) space solution
    def isPalindrome(self, head: ListNode) -> bool:
        # reverse the first half of the linked list and compare if the two halves equals
        
        # compute length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        # reverse the first half
        skip_count = length // 2
        prev = None
        while skip_count > 0:
            skip_count -= 1
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        # traverse two halves at the same time and check if two equals
        if length % 2:
            head = head.next
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True