class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # use dp because of "maximum" score and overlapping subproblems
        # dp(i, left) for returning maximum score so far
        # dp(i, left) = max(mul[i] * nums[left] + dp(i + 1, left + 1), 
        #                   mul[i] * nums[right] + dp(i + 1, left))
        #               where right = len(nums) - 1 - (i - left)
        # if i == len(multipliers): dp() returns 0
        
        # memo = {}
        # def dp(i, left):
        #     if i == len(multipliers):
        #         return 0
        #     if (i, left) not in memo:
        #         right = len(nums) - 1 - (i - left)
        #         memo[(i, left)] = max(
        #             multipliers[i] * nums[left] + dp(i + 1, left + 1),
        #             multipliers[i] * nums[right] + dp(i + 1, left)
        #         )
        #     return memo[(i, left)]
        # return dp(0, 0)
        # -> TLE!!!
        
        # @functools.lru_cache(None)
        # def dp(i, left):
        #     if i == len(multipliers):
        #         return 0
        #     right = len(nums) - 1 - (i - left)
        #     return max(
        #         multipliers[i] * nums[left] + dp(i + 1, left + 1),
        #         multipliers[i] * nums[right] + dp(i + 1, left)
        #     )
        # ans = dp(0, 0)
        # dp.cache_clear()
        # return ans
        
        # bottom-up: iterative solution
        dp = [[0] * (len(multipliers) + 1) for _ in range(len(multipliers) + 1)]
        for i in range(len(multipliers) - 1, -1, -1):
            for left in range(i, -1, -1):
                right = len(nums) - 1 - (i - left)
                dp[i][left] =  max(
                    multipliers[i] * nums[left] + dp[i + 1][left + 1],
                    multipliers[i] * nums[right] + dp[i + 1][left]
                )
        return dp[0][0]
    