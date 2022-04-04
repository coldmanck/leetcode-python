class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # can use DFS, BFS or disjoing set
        
        # Solution (DFS)
        # time: O(V + E)
        # space: O(V + E) because of the construction of graph via an adjacency matrix; otherwise, O(V)
        if source == destination:
            return True
        
        ### construct adjacency matrix
        # graph = [[0] * n for _ in range(n)]
        # for edge in edges:
        #     graph[edge[0]][edge[1]] = graph[edge[1]][edge[0]] = 1
        # construct graph dict
        from collections import defaultdict
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        ### DFS
        # stack = [source]
        # visited = set()
        # while stack:
        #     node = stack.pop()
        #     visited.add(node)
        #     # for i in range(n):
        #     for i in graph[node]:
        #         # if i == node:
        #         #     continue
        #         # if graph[node][i] == 1 and i not in visited:
        #         if i not in visited:
        #             if i == destination:
        #                 return True
        #             stack.append(i)
        # return False
        
        ### BFS
        from collections import deque
        queue = deque([source])
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                if neighbor == destination:
                    return True
                queue.append(neighbor)
        return False