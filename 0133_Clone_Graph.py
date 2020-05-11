# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''Stack iterative solution'''
        if not node:
            return None
        visited = {node: Node(node.val)}
        stack = [node]
        head = node
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited[neighbor] = Node(neighbor.val)
                visited[node].neighbors.append(visited[neighbor])
        return visited[head]
        
        '''Recursion solution'''
#         visited = {}
#         def clone_graph(node, visited):
#             if not node:
#                 return None
#             if node in visited:
#                 return visited[node]
#             new_node = Node(node.val)
#             visited[node] = new_node
#             new_node.neighbors = [clone_graph(neighbor, visited) for neighbor in node.neighbors]
#             return new_node
        
#         return clone_graph(node, visited)
        