# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy_head = ListNode(-1)
        head = dummy_head
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                val %= 10
                carry = 1
            else:
                carry = 0
            head.next = ListNode(val)
            head = head.next
        
        if carry:
            head.next = ListNode(carry)
        
        return dummy_head.next