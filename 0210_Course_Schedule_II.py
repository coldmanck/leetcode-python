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
        
        # topological order
        # time: O(E+V)
        # space: O(V+E)
        '''
        in_deg = [0] * numCourses
        from collections import defaultdict
        graph = defaultdict(list)
        for target, source in prerequisites:
            graph[source].append(target)
            in_deg[target] += 1
        
        from collections import deque
        queue = deque([i for i in range(numCourses) if in_deg[i] == 0])
        sol = []
        while queue:
            course = queue.popleft()
            sol.append(course)
            for nbr in graph[course]:
                in_deg[nbr] -= 1
                if in_deg[nbr] == 0:
                    queue.append(nbr)
        return sol if len(sol) == numCourses else []
        '''