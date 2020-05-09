# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''Method 1: use dummy head to write cleaner code!'''
        dummy_head = ListNode(-1)
        dummy_head.next = head
        node = dummy_head
        while node.next:
            if node.next.val == val:
                to_del = node.next
                node.next = node.next.next
                del to_del
            else:
                node = node.next
        return dummy_head.next
        
        '''Method 2'''
        # while head and head.val == val:
        #     node = head
        #     head = head.next
        #     del node
        # node = head
        # while node:
        #     if node.next and node.next.val == val:
        #         to_del = node.next
        #         node.next = node.next.next
        #         del to_del
        #     else:
        #         node = node.next
        # return head
    
    