class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp(i) means the min cost to pass through the current staircase
        # - note that we additionally add an element 0 to the end of the array
        # recurrence relation: dp(i) = min(dp(i - 1), dp(i - 2)) + cost[i]
        # base cases: dp(0) = cost[0], dp(1) = cost[1]
        
        # memo = {}
        # cost.append(0)
        # def dp(i):
        #     if i < 2:
        #         return cost[i]
        #     if i not in memo:
        #         memo[i] = min(dp(i - 1), dp(i - 2)) + cost[i]
        #     return memo[i]
        # return dp(len(cost) - 1)
        
        # cost.append(0)
        # dp = [0] * (len(cost))
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # for i in range(2, len(cost)):
        #     dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        # return dp[-1]
        
        # O(n) time O(1) space
        # dp = [0] * (len(cost) + 1)
        two_back, one_back = cost[0], cost[1]
        for i in range(2, len(cost)):
            one_back, two_back = min(one_back, two_back) + cost[i], one_back
        return min(one_back, two_back)