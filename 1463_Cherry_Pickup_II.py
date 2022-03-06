from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # solving for maximum values + past decisions affect futures -> use dp!
        # dp(i, j1, j2) returns the maximum cherry counts from both in grid[i:][:]
        # - to return the answer: dp(0, 0, len(grid[0]) - 1)
        # dp(i, j1, j2) = max(dp(i - 1, j1 - 1, j2), dp(i - 1, j1, j2), dp(i - 1, j1 + 1, j2),
        #                     dp(i - 1, j1, j2 - 1), dp(i - 1, j1, j2), dp(i - 1, j1, j2 + 1))
        # base cases: dp(len(grid) - 1, j1, j2) = grid[len(grid) - 1][j1] + grid[len(grid) - 1][j2]
        
        @lru_cache(None)
        def dp(i, j1, j2):
            if j1 < 0 or j1 > len(grid[0]) - 1 or j2 < 0 or j2 > len(grid[0]) - 1:
                return float('-inf')
            ans = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
            if i != len(grid) - 1:
                ans += max(dp(i + 1, new_j1, new_j2) for new_j1 in [j1 - 1, j1, j1 + 1] for new_j2 in [j2 - 1, j2, j2 + 1])
            return ans
        return dp(0, 0, len(grid[0]) - 1)