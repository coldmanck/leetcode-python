class MyLinkedList:
    class Node:
        def __init__(self, val=-1, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.head
        for i in range(index + 1):
            node = node.next
            if node is self.tail:
                return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = self.Node(val)
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.Node(val)
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node
        node.next = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = self.head
        for i in range(index + 1):
            node = node.next
            if node is self.tail:
                if i == index:
                    self.addAtTail(val)
                    return
                else:
                    return
        new_node = self.Node(val)
        new_node.next = node
        new_node.prev = node.prev
        node.prev.next = new_node
        node.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self.head
        for i in range(index + 1):
            node = node.next
            if node is self.tail:
                return
        node.prev.next = node.next
        node.next.prev = node.prev
        del node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)