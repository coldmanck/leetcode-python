class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indeg = {i:[] for i in range(numCourses)}, {i:0 for i in range(numCourses)}
        for end, start in prerequisites:
            graph[start].append(end)
            indeg[end] += 1
        from collections import deque
        queue = deque([node for node, deg in indeg.items() if deg == 0])
        visited = set()
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    return []
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
        return ans if len(visited) == numCourses else []    
        