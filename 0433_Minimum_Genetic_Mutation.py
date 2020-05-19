class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        from collections import defaultdict, deque
        if not end in bank:
            return -1
        
        def dist(a, b):
            d = 0
            for k in range(len(a)):
                if a[k] != b[k]:
                    d += 1
            return d
        
        # dist = defaultdict(dict)
        graph = defaultdict(list)
        bank = list(set(bank))
        for i in range(len(bank)):
            for j in range(len(bank)):
                if i == j:
                    continue
                if dist(bank[i], bank[j]) == 1:
                    graph[bank[i]].append(bank[j])
        
        # bank = set(bank)
        # find the 1-dist away string in the bank as starting point
        new_start = ''
        for s in bank:
            if dist(start, s) == 1:
                new_start = s
                ans = 1
                break
        if not new_start:
            return False
        
        queue = deque()
        queue.append((new_start, 1))
        visited = set([new_start])
        while queue:
            s, mut = queue.popleft()
            if s == end:
                return mut
            for nb in graph[s]:
                if nb not in visited:
                    queue.append((nb, mut + 1))
                    visited.add(nb)
        return -1