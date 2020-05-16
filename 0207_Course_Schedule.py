from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        graph, indeg = {i:[] for i in range(numCourses)}, {i:0 for i in range(numCourses)}
        for end, start in prerequisites:
            graph[start].append(end)
            indeg[end] += 1
        
        # output topological ordering
        queue = deque([node for node, deg in indeg.items() if deg == 0])
        visited = set() # or use set(queue)
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited: # then a circle found
                    return False
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
        return len(visited) == numCourses