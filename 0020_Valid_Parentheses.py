# Runtime: 52 ms, faster than 5.66% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')':'(', ']':'[', '}':'{'}
        stack = []
        for ch in s:
            if ch not in parentheses:
                stack.append(ch)
            else:
                if not stack or stack.pop() != parentheses[ch]:
                    return False
        return not stack