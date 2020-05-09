# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        # compute the length of each seq
        lenA = lenB = 1
        nodeA = headA
        while nodeA.next:
            nodeA = nodeA.next
            lenA += 1
        nodeB = headB
        while nodeB.next:
            nodeB = nodeB.next
            lenB += 1
        
        if lenA < lenB: # make sure seq A is longer or equal to seq B
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        for i in range(lenA - lenB): # move only the seqA part longer than seq B forward
            headA = headA.next
        while headA and headB and headA != headB: # find the intersection
            headA = headA.next
            headB = headB.next
        return headA