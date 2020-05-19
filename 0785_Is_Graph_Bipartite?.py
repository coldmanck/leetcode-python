class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # can be translated into graph (two-)coloring problem
        '''DFS'''
        # def dfs_color(i):
        #     for nb in graph[i]:
        #         if nb in color:
        #             if color[nb] == color[i]:
        #                 return False
        #         else:
        #             color[nb] = 1 - color[i]
        #             if not dfs_color(nb):
        #                 return False
        #     return True
        # color = {}
        # for i in range(len(graph)):
        #     if i not in color:
        #         color[i] = 0
        #         if not dfs_color(i):
        #             return False
        # return True
        
        '''BFS'''
        from collections import deque
        queue = deque()
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                queue.append(i)
                while queue:
                    node = queue.popleft()
                    for nb in graph[node]:
                        if nb in color:
                            if color[nb] == color[node]:
                                return False
                        else:
                            color[nb] = 1 - color[node]
                            queue.append(nb)
        return True