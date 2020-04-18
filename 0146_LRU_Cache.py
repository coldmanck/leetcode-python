'''
Approach 1: use OrderedDict
Runtime: 184 ms, faster than 82.02% of Python3 online submissions for LRU Cache.
Memory Usage: 22.9 MB, less than 6.06% of Python3 online submissions for LRU Cache.
'''

# from collections import OrderedDict
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.data = OrderedDict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key in self.data:
#             ans = self.data[key]
#             self.data.move_to_end(key)
#         else:
#             ans = -1
#         return ans

#     def put(self, key: int, value: int) -> None:
#         result = self.get(key)
#         if result > 0:
#             self.data[key] = value
#             self.data.move_to_end(key)
#         else:
#             if len(self.data) == self.capacity:
#                 self.data.popitem(last=False)
#             self.data[key] = value

'''
Approach 2: Doubly linked list + Hash map
Runtime: 312 ms, faster than 19.90% of Python3 online submissions for LRU Cache.
Memory Usage: 23.2 MB, less than 6.06% of Python3 online submissions for LRU Cache.
'''
class DLListHashMapNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.head, self.tail = DLListHashMapNode(), DLListHashMapNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.data = {} # {key=key, value=node in linked list}
        self.capacity = capacity

    def move_to_end(self, node): # move to tail
        node.prev.next = node.next
        node.next.prev = node.prev
        
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def popitem(self): # pop from head
        node = self.head.next
        next = node.next
        
        self.head.next = next
        next.prev = self.head
        node.next = node.prev = None
        
        del self.data[node.key]
        return node.val

    def additem(self, key, val):
        node = DLListHashMapNode(key=key, val=val)
        prev = self.tail.prev
        
        prev.next = self.tail.prev = node
        node.prev = prev
        node.next = self.tail
        
        self.data[key] = node

    def get(self, key):
        if key in self.data:
            node = self.data[key]
            self.move_to_end(node)
            return node.val
        else:
            return -1

    def put(self, key, val):
        if key in self.data:
            node = self.data[key]
            node.val = val
            self.move_to_end(node)
        else:
            if len(self.data) == self.capacity:
                self.popitem()
            self.additem(key, val)