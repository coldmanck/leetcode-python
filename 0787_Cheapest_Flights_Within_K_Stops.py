class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))
        visited = set()
        heap = [(0, 0, src)] # [cost, n_transits, node]
        while heap:
            cost, n_transits, node = heapq.heappop(heap)
            if node == dst:
                return cost
            visited.add(node)
            for neighbor, neighbor_cost in graph[node]:
                if not neighbor in visited and n_transits <= K: # len of path = K + 1
                    heapq.heappush(heap, (cost + neighbor_cost, n_transits + 1, neighbor))
        return -1