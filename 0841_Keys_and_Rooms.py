class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # connected components: use DFS/BFS to traverse
        from collections import deque
        queue = deque([0])
        visited = set([0])
        while queue:
            idx = queue.popleft()
            for neighbor in rooms[idx]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited) == len(rooms)