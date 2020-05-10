# Runtime: 68 ms, faster than 87.39% of Python3 online submissions for Design Circular Queue.
# Memory Usage: 14.5 MB, less than 5.26% of Python3 online submissions for Design Circular Queue.

class MyCircularQueue:
    class Node:
        def __init__(self, val, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.count = 0
        self.front = self.Node(-1)
        self.rear = self.Node(-1)
        self.front.next = self.rear
        self.rear.prev = self.front
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.capacity == self.count:
            return False
        self.count += 1
        
        node = self.Node(value)
        self.rear.prev.next = node
        node.prev = self.rear.prev
        node.next = self.rear
        self.rear.prev = node
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.count -= 1
        
        node = self.front.next
        self.front.next = node.next
        node.next.prev = self.front
        del node
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.front.next.val

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count == 0:
            return -1
        return self.rear.prev.val
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if self.count == 0 else False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return True if self.count == self.capacity else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()