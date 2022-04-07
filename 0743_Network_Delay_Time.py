# Runtime: 484 ms, faster than 81.40% of Python3 online submissions for Network Delay Time.
# Memory Usage: 15.6 MB, less than 7.69% of Python3 online submissions for Network Delay Time.

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        '''Time O((E+V)logV) Space O(V+E)'''
        from collections import defaultdict
        import heapq
        graph = defaultdict(list) # space O(E)
        for u, v, w in times: # Time O(E)
            graph[u].append((v, w))
        visited = set()
        heap = [(0, K)] # [cost from the source node K, node id]
        while heap and len(visited) < N: # while loop: total time O(E * logV)
            cost, node = heapq.heappop(heap) # time O(logV) space O(V)
            if node in visited:
                continue
            visited.add(node)
            for nbr, cost_nbr in graph[node]:
                if not nbr in visited:
                    heapq.heappush(heap, (cost + cost_nbr, nbr)) # O(logV)
        return cost if len(visited) == N else -1