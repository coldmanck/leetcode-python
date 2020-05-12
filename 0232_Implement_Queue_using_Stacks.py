class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front1 = None
        self.front2 = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # time O(1)
        self.stack1.append(x)
        if not self.front1:
            self.front1 = x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # time amortized O(1) (worst O(n))
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.front1 = None
        val = self.stack2.pop()
        self.front2 = self.stack2[-1] if self.stack2 else None
        return val
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front2 or self.front1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.front2 and not self.front1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()