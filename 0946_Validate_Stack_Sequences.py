class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack_set = set()
        stack = []
        i = j = 0
        while i < len(pushed) and j < len(popped):
            while i < len(pushed) and popped[j] not in stack_set:
                stack.append(pushed[i])
                stack_set.add(pushed[i])
                i += 1
            while j < len(popped) and popped[j] in stack_set:
                if popped[j] != stack[-1]:
                    return False
                stack.pop()
                stack_set.remove(popped[j])
                j += 1
        return True