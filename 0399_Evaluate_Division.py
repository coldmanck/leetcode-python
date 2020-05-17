class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # floyd-warshall algorithm
        # Time O(V^3) Space O(V^2)
        from collections import defaultdict
        graph = defaultdict(dict)
        for (num, den), val in zip(equations, values):
            graph[num][den] = val
            graph[den][num] = 1 / val
            graph[num][num] = graph[den][den] = 1.0
        # for k in graph:
        #     for i in graph[k]:
        #         for j in graph[k]:
        #             graph[i][j] = graph[i][k] * graph[k][j]
        import itertools
        for k, i, j in itertools.permutations(graph, 3):
            if k in graph[i] and j in graph[k]:
                graph[i][j] = graph[i][k] * graph[k][j]
        return [graph[num].get(den, -1.0) for num, den in queries]