class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = cur_num = ''
        for ch in s:
            if ch == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = cur_num = ''
            elif ch == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + int(num) * cur_str
            elif ch.isdigit():
                cur_num += ch
            else: # ch.isalpha
                cur_str += ch
        return cur_str