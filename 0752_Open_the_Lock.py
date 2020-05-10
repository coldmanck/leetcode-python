class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        # solve a 4-d coordinate maze with BFS (guaranteed the shortest path found in an undirected graph)
        directions = []
        k = 4
        for i in range(k):
            for j in (1, -1):
                directions.append([0] * i + [j] + [0] * (k - 1 - i))
        print(directions)
        
        from collections import deque
        queue = deque()
        queue.append((0, 0, 0, 0, 0))
        deadends = set(deadends)
        cache = set()
        while queue:
            i, j, k, l, count = queue.popleft()
            print(i, j, k, l)
            if ''.join([str(i), str(j), str(k), str(l)]) == target:
                return count
            for ii, jj, kk, ll in directions:
                # i2 = (i + ii) % 10 if i + ii > 10 else ((i + ii + 10) if i + ii < 0 else i + ii)
                # j2 = (j + jj) % 10 if j + jj > 10 else ((j + jj + 10) if j + jj < 0 else j + jj)
                # k2 = (k + kk) % 10 if k + kk > 10 else ((k + kk + 10) if k + kk < 0 else k + kk)
                # l2 = (l + ll) % 10 if l + ll > 10 else ((l + ll + 10) if l + ll < 0 else l + ll)
                i2, j2, k2, l2 = (i + ii) % 10, (j + jj) % 10, (k + kk) % 10, (l + ll) % 10
                s = ''.join([str(i2), str(j2), str(k2), str(l2)])
                if s in cache or s in deadends:
                    continue
                cache.add(s)
                queue.append((i2, j2, k2, l2, count + 1))
        return -1
            