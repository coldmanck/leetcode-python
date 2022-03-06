from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. use dp because of finding the minimum amount of coins needed &
        #    past decision affect futures'
        # 2. dp(amount, coins) return the minimum number of coins needed
        # 3. recurrence relation: dp(amount, coins) = 1 + min(
        #                          [dp(amount - c) for c in coins]
        #                      )
        # 4. base cases: dp(0) = 0 / if amount < 0: return float('inf')
        
        @lru_cache(None)
        def dp(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            return 1 + min([dp(amount - c) for c in coins])
        ans = dp(amount)
        return ans if ans != float('inf') else -1