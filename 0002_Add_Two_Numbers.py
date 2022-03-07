# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # iterative solution in 2020
        '''
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
        '''

        # recursive solution in 2022
        def helper(l1, l2, carry_on):
            if not l1 and not l2:
                return ListNode(carry_on) if carry_on > 0 else None
            added_val = carry_on
            if l1:
                added_val += l1.val
            if l2:
                added_val += l2.val
            carry_on = added_val // 10
            added_val %= 10
            return ListNode(added_val, helper(l1.next if l1 else None, l2.next if l2 else None, carry_on))
        
        return helper(l1, l2, 0)