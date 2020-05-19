class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        from collections import deque, defaultdict
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        queue = deque()
        color = {}
        for i in range(N):
            if not i in color:
                color[i] = 0
                queue.append(i)
                while queue:
                    j = queue.popleft()
                    for nb in graph[j]:
                        if nb in color:
                            if color[nb] == color[j]:
                                return False
                        else:
                            color[nb] = 1 - color[j]
                            queue.append(nb)
        return True