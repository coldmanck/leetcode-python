# Runtime: 484 ms, faster than 81.40% of Python3 online submissions for Network Delay Time.
# Memory Usage: 15.6 MB, less than 7.69% of Python3 online submissions for Network Delay Time.

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        '''Time O(V+ElogE) Space O(V+E)'''
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for u, v, w in times: # Time O(V)
            graph[u].append((v, w))
        visited = set()
        heap = [(0, K)] # [cost, node]
        while heap and len(visited) < N: # Time O(ElogE)
            cost, node = heapq.heappop(heap) # O(logE)
            if node in visited:
                continue
            visited.add(node)
            for nbr, cost_nbr in graph[node]:
                if not nbr in visited:
                    heapq.heappush(heap, (cost + cost_nbr, nbr)) # O(logE)
        return cost if len(visited) == N else -1