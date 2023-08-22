from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # initialize adjacent list
        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        # initialize leaves queue
        leaves = deque()
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)

        # BFS until n <= 2
        while n > 2:
            n -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return leaves
        # time = space = O(n)