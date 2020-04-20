# Runtime: 52 ms, faster than 5.66% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        open_parantheses = set(['(', '[', '{'])
        dict_parantheses = {')':'(', ']':'[', '}':'{'}
        
        for ch in s:
            if ch in open_parantheses:
                stack.append(ch)
            else:
                if len(stack) == 0 or stack.pop() != dict_parantheses[ch]:
                    return False
        
        return len(stack) == 0