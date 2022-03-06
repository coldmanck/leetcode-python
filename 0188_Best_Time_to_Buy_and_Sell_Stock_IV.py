from functools import lru_cache
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # use dp because of finding maximum profit & past decision affect futures'
        # dp(i, n_possible_trans, is_hold) returns the max. profit starting from day $i
        #     with $n_possible_trans transcations left and if $is_hold a stock
        #     return d(0, k, 0) for the answer
        # recurrence relation: dp(i, n_possible_trans, is_hold) = max(
        #                          -prices[i] + dp(i + 1, n_possible_trans, is_hold), # buy
        #                          dp(i + 1, n_possible_trans, is_hold), # do nth
        #                      ) if is_hold == 0 else max(
        #                          prices[i] + dp(i + 1, n_possible_trans - 1, is_hold), # sell
        #                          dp(i + 1, n_possible_trans, is_hold), # do nth
        #                      )
        # base cases: i == len(prices): return 0 / n_possible_trans == 0: return 0
        
        @lru_cache(None)
        def dp(i, n_possible_trans, is_hold):
            if i == len(prices) or n_possible_trans == 0:
                return 0
            return max(
                 -prices[i] + dp(i + 1, n_possible_trans, 1), # buy
                 dp(i + 1, n_possible_trans, 0), # do nth
             ) if is_hold == 0 else max(
                 prices[i] + dp(i + 1, n_possible_trans - 1, 0), # sell
                 dp(i + 1, n_possible_trans, 1), # do nth
             )
        return dp(0, k, 0)
    
        # time/space complexity is the number of states: O(n°k*2) = O(n*k)