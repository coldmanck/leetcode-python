class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop() # pop '['
                temp.reverse()
                nb, ratio = 0, 1
                while stack and len(stack[-1]) == 1 and 0 <= ord(stack[-1]) - ord('0') <= 9:
                    nb += ratio * int(stack.pop())
                    ratio *= 10
                stack.append(''.join(nb * temp))
        return ''.join(stack)