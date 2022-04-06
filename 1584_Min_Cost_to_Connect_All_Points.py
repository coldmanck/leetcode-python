class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def union(self, a, b):
        # union by rank
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.root[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.root[root_a] = root_b
            else:
                self.root[root_b] = root_a
                self.rank[root_a] += 1
        
    def find(self, a):
        # path compression
        if a == self.root[a]:
            return a
        self.root[a] = self.find(self.root[a])
        return self.root[a]
    
    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Solution 1: Kruskal's alrorithm
        # 1. sort the edges according to the weights (in increasing order)
        def comp_dist(p1, p2):
            return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
        edges = [(a, b, comp_dist(a, b)) for a in range(len(points) - 1) for b in range(a + 1, len(points))]
        edges.sort(key=lambda x: x[2])
        
        # 2. link the edges without loops
        # 3. stop when there're n - 1 edges
        total_dist = n_edges = 0
        uf = UnionFind(len(points))
        for edge in edges:
            a, b, dist = edge
            if not uf.is_connected(a, b):
                uf.union(a, b)
                n_edges += 1
                total_dist += dist
                if n_edges == len(points) - 1:
                    return total_dist
        return 0