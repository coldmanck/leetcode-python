class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    val = b + a
                elif token == '-':
                    val = b - a
                elif token == '*':
                    val = b * a
                else:
                    # refrain from using // (floor) as it produces unwanted results for negative nb.
                    val = int(b / a)
                stack.append(val)
        return stack[-1]