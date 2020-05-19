class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        from collections import deque
        queue = deque()
        visited = set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not (i, j) in visited:
                    cur_area = 0
                    visited.add((i, j))
                    queue.append((i, j))
                    while queue:
                        i2, j2 = queue.popleft()
                        cur_area += 1
                        for ii, jj in directions:
                            i3, j3 = i2 + ii, j2 + jj
                            if 0 <= i3 < len(grid) and 0 <= j3 < len(grid[0]) and grid[i3][j3] == 1 and not (i3, j3) in visited:
                                visited.add((i3, j3))
                                queue.append((i3, j3))
                    max_area = max(max_area, cur_area)
        return max_area