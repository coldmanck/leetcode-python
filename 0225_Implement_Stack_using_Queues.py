from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.rear = None

    def push(self, x: int) -> None: # O(1)
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.rear = x

    def pop(self) -> int: # O(n)
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(len(self.queue) - 1):
            val = self.queue.popleft()
            self.queue.append(val)
        self.rear = val if len(self.queue) > 1 else None
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.rear
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()