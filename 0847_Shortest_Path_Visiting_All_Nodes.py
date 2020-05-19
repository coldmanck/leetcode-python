class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # BFS with deque
        from collections import deque
        queue = deque([(i, 0, 1 << i) for i in range(len(graph))]) # (node, cost, state)
        visited = set() # actualy should be set((i, 1 << i) for i in range(len(graph))), but it's impossible to reach
        final_state = (1 << len(graph)) - 1
        while queue:
            node, cost, state = queue.popleft()
            if state == final_state:
                return cost
            for neighbor in graph[node]:
                if (neighbor, state | (1 << neighbor)) not in visited:
                    visited.add((neighbor, state | (1 << neighbor)))
                    queue.append((neighbor, cost + 1, state | (1 << neighbor)))
        
        # backtrack start from the node with minimal degree
        # start, min_edges = 0, float('inf')
        # for i, edges in enumerate(graph):
        #     if len(edges) == 1:
        #         start = i
        #         break
        #     if len(edges) < min_edges:
        #         start, min_edges = i, len(edges)
        # visited = set()
        # visited.add(start)
        # # print(start)
        # def backtrack(node, count):
        #     # print(node, count)
        #     if len(visited) == len(graph):
        #         return count, True
        #     for neighbor in graph[node]:
        #         if not neighbor in visited:
        #             visited.add(neighbor)
        #             count, is_finished = backtrack(neighbor, count + 1)
        #             if is_finished:
        #                 return count, is_finished
        #     return count + 1, False
        # return backtrack(start, 0)[0]