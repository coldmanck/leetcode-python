# Runtime: 152 ms, faster than 45.13% of Python3 online submissions for Number of Islands.
# Memory Usage: 14.1 MB, less than 22.22% of Python3 online submissions for Number of Islands.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check_island_size(i, j):
            if not(0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] == '0' or cache[i][j] == -2:
                return
            cache[i][j] = -2
            check_island_size(i-1, j)
            check_island_size(i+1, j)
            check_island_size(i, j-1)
            check_island_size(i, j+1)
        
        # use a cache matrix where -1 means haven't traverse -2 means traversed
        cache = [[-1] * len(grid[0]) for _ in range(len(grid))]
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if cache[i][j] == -2 or grid[i][j] == '0':
                    continue
                
                count += 1
                check_island_size(i, j)
        
        return count