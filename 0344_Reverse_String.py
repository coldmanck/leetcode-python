# Runtime: 168 ms, faster than 90.57% of Python online submissions for Reverse String.
# Memory Usage: 18.8 MB, less than 37.50% of Python online submissions for Reverse String.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right -1