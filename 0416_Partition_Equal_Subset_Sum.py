from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False

        # DP 1: top-down DP (memoization)
        '''
        @lru_cache(maxsize=None)
        def dp(cur_idx, remain_sum):
            if remain_sum == sum_nums // 2:
                return True
            if remain_sum < sum_nums // 2 or cur_idx >= len(nums):
                return False
            return dp(cur_idx + 1, remain_sum) or dp(cur_idx + 1, remain_sum - nums[cur_idx])

        return dp(0, sum_nums)
        '''

        # DP 2: bottom-up DP
        target = sum_nums // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]