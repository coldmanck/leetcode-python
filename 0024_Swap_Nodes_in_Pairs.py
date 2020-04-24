# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # INCORRECT to assume that there are even number of nodes
        '''Method 1: recursive
        Runtime: 28 ms, faster than 74.82% of Python3 online submissions for Swap Nodes in Pairs.
        Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Swap Nodes in Pairs.
        '''
        # if not head or not head.next:
        #     return head
        # new_head = head.next
        # head.next = self.swapPairs(new_head.next)
        # new_head.next = head
        # return new_head
        
        '''Method 2: iterative
        Runtime: 32 ms, faster than 43.01% of Python3 online submissions for Swap Nodes in Pairs.
        Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Swap Nodes in Pairs.
        '''
        node = new_head = head
        if node and node.next:
            new_head = node.next
        while node and node.next:
            next_head = node.next.next
            node.next.next = node
            node.next = next_head.next if next_head and next_head.next else next_head
            node = next_head
        return new_head