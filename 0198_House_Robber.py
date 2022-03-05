class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP 1: top-down
        '''
        # dp(i): means the maximum number of money can be robbed so far from [0, i]
        # recurrence relation: dp(i) = max(dp(i-1), dp(i-2) + nums[i])
        # base cases: dp(0) = nums[0], dp(1) = max(nums[0], nums[1]))
        memo = {} 
        
        def dp(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]
        
        return dp(len(nums) - 1)
        '''
        # DP 2: bottom-up
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]