# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self,  head: 'Node') -> 'Node':
        '''Approach 1: iterative time & space O(n)
        Runtime: 40 ms, faster than 21.26% of Python3 online submissions for Copy List with Random Pointer.
        Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.
        '''
        if not head:
            return head
        
        node = head
        new_node = Node(head.val)
        hash_map_node = {node:new_node}
        while node:
            if node.random:
                if not node.random in hash_map_node:
                    hash_map_node[node.random] = Node(node.random.val)
                new_node.random = hash_map_node[node.random]
            if node.next:
                if not node.next in hash_map_node:
                    hash_map_node[node.next] = Node(node.next.val)
                new_node.next = hash_map_node[node.next]
            node = node.next
            new_node = new_node.next
        return hash_map_node[head]

        '''Approach 2: Recursive time & space O(n)
        Runtime: 40 ms, faster than 21.26% of Python3 online submissions for Copy List with Random Pointer.
        Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.

        Time Complexity: O(N) where N is the number of nodes in the linked list.
        Space Complexity: O(N). If we look closely, we have the recursion stack and we also have the space complexity to keep track of nodes already cloned i.e. using the visited dictionary. But asymptotically, the complexity is O(N).
        '''
        '''
        if not head:
            return head
        
        hash_map_node = {} # key of old objects, value of new objects
        def deepcopy(node):
            if not node:
                return None
            if node in hash_map_node:
                return hash_map_node[node]
            
            new_node = Node(node.val)
            new_node.next = deepcopy(node.next)
            new_node.random = deepcopy(node.random)
            hash_map_node[node] = new_node
            return new_node
        
        return deepcopy(head)
        '''
