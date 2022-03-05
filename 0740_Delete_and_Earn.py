from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # can be reduced to the House Robber problem
        golds = [0] * 10001
        for num in nums:
            golds[num] += num
        memo = {}
        
        def dp(i):
            if i == 0:
                return golds[0]
            if i == 1:
                return max(golds[0], golds[1])
            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + golds[i])
            return memo[i]
        ans = dp(len(golds) - 1)
        print(memo)
        return ans