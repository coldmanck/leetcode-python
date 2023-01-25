# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Implementaion I: reverse the first half of the linked list and compare if the two halves equals
        '''
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
        '''

        # Implementaion II: O(n) time O(n) space
        '''
        nums = []
        cur = head
        while cur is not None:
            nums.append(cur.val)
            cur = cur.next
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != nums[right]:
                return False
            left, right = left + 1, right - 1
        return True
        '''

        # Implementaion III: O(n) time O(1) space
        # Ref.: https://leetcode.com/problems/palindrome-linked-list/solutions/1137027/js-python-java-c-easy-floyd-s-reversal-solution-w-explanation/
        # find the middle location
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # reverse the second half linked list
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        front, tail = head, prev
        while front and tail:
            if front.val != tail.val:
                return False
            front, tail = front.next, tail.next
        return True