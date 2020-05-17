import heapq, collections

City = collections.namedtuple('City', ('cost', 'city_name', 'path'))

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(set)
        for edge in times:
            graph[edge[0]].add((edge[1], edge[2]))

        city_heap = [City(0, K, ())]
        visited = set()
        mins = {K: 0}
        while city_heap:
            city1 = heapq.heappop(city_heap)
            if city1.city_name in visited:
                continue
            ans = city1.cost
            visited.add(city1.city_name)
            path = (city1.path, city1.city_name)

            for city2_name, weight in graph[city1.city_name]:
                if city2_name in visited:
                    continue
                prev_cost = mins.get(city2_name, None)
                new_cost = weight + city1.cost
                if prev_cost is None or new_cost < prev_cost:
                    mins[city2_name] = new_cost
                    heapq.heappush(city_heap, City(new_cost, city2_name, path))

        return ans if len(visited) == N else -1