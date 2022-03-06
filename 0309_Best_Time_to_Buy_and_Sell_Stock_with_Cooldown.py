from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp(i, is_hold, is_cool) returns maxProfit starting from day $i & $is_hold -ing stock
        # & if under the cooling period ($is_cool)
        # return dp(0, 0, 0) for the final answer
        # recurrence relation: dp(i, is_hold, is_cool) = 
        #                    if is_cool: return dp(i + 1, is_hold, 0)
        #                    else: if is_hold: return max(prices[i] + dp(i + 1, 0, 1), dp(i + 1, 1, 0))
        #                          else: return max(-prices[i] + dp(i + 1, 1, 0), dp(i + 1, 0, 0))
        # base cases: if i == len(prices): return 0
        
        @lru_cache(None)
        def dp(i, is_hold, is_cool):
            if i == len(prices):
                return 0
            if is_cool:
                return dp(i + 1, is_hold, 0)
            if is_hold:
                return max(
                    prices[i] + dp(i + 1, 0, 1), # sell & cool
                    dp(i + 1, 1, 0) # do nth
                )
            return max(
                -prices[i] + dp(i + 1, 1, 0), # buy
                dp(i + 1, 0, 0) # do nth
            )
        return dp(0, 0, 0)

        # time/space complexity is the number of states: O(len(prices)*2)