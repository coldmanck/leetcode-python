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
        def comp_dist(p1, p2):
            return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
        
        # Solution 1: Kruskal's alrorithm
        # time complexity: O(ElogE) + O(E * \alpha(V)) = O(ElogE)
        # space complexity: O(logE) + O(V)
        '''
        # 1. sort the edges according to the weights (in increasing order)
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
        '''
        
        # Solution 2: Prim's algorithm
        # time complexity: O((V+E)*logV)
        # space complexity: O(V)
        # 1. maintain two sets: visited and unvisited. initialize visited with the start vertex.
        import heapq
        heap = [] # (min_dist_to_cur_set, node_a, node_b)
        visited = set()
        visited.add(0)
        unvisited = set(range(len(points))) - visited
        for i in range(1, len(points)):
            heap.append((comp_dist(0, i), 0, i))
        heapq.heapify(heap)
        
        total_dist = 0
        while len(visited) < len(points):
            min_dist, _, node_b = heapq.heappop(heap)
            while node_b in visited:
                min_dist, _, node_b = heapq.heappop(heap)
            
            total_dist += min_dist
            visited.add(node_b)
            unvisited.remove(node_b)
            for i in unvisited:
                heapq.heappush(heap, (comp_dist(node_b, i), node_b, i))
        return total_dist
        
        # 2. for the neighbors of each vertex in the visited set, pick the `nearest` one to 
        #    add to the visited set ("grow" the MST)
        # 3. stop until the unvisited sets is empty
        