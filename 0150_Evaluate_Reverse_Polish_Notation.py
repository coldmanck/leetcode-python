class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                # refrain from using // (floor) as it produces unwanted results for negative nb.
                stack.append(str(int(eval(a+token+b)))) 
            else:
                stack.append(token)
        return int(stack[0])