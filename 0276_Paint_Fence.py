from functools import lru_cache
class Solution:
    def numWays(self, n: int, k: int) -> int:
        # use dp to find the number of different ways to paint fence
        # dp(i) to return the number of ways of painting the fence up to $i-th posts (0-indexed).
        # return dp(n-1) for the final answer
        # recurrence relation: 
        # - can paint the i-th post a color different from (i-1)-th one: (k - 1) * dp(i - 1) ways
        # - OR paint the i-th post a color same as the (i-1)-th one, subject to different from the (i-2)-th one:
        #.  1 * (k - 1) * dp(i - 2) ways
        # - total number of ways = (k - 1) * (dp(i - 1) + dp(i - 2))
        # base cases: dp(0) = k, dp(1) = k ** 2
        
        @lru_cache(None)
        def dp(i):
            if i <= 1:
                return k ** (i + 1)
            return (k - 1) * (dp(i - 1) + dp(i - 2))
        return dp(n - 1)
    
    # time/space complexity = O(n)