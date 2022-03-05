class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''Recursion with memoization'''
        cache = {} # key of (idx, cur_sum), value of n_sol
        def helper(idx, cur_sum, cache):
            if idx == len(nums):
                if cur_sum == S:
                    return 1
                return 0
            if (idx, cur_sum) not in cache:
                pos = helper(idx + 1, cur_sum + nums[idx], cache)
                neg = helper(idx + 1, cur_sum - nums[idx], cache)
                cache[(idx, cur_sum)] = pos + neg
            return cache[(idx, cur_sum)]
        
        return helper(0, 0, 0, cache)
        
        '''Brute force (Recursion): TLE O(2^n)'''
        # def helper(idx, cur_sum, n_sol, remain_sum):
        #     if idx == len(nums):
        #         if cur_sum == S:
        #             return n_sol + 1
        #         return n_sol
        #     # working on nums[idx:]
        #     diff = abs(S - cur_sum)
        #     if diff > remain_sum:
        #         return n_sol
        #     if cur_sum <= S or diff <= remain_sum:
        #         n_sol = helper(idx + 1, cur_sum + nums[idx], n_sol, remain_sum - nums[idx])
        #     if cur_sum >= S or diff <= remain_sum:
        #         n_sol = helper(idx + 1, cur_sum - nums[idx], n_sol, remain_sum - nums[idx])
        #     return n_sol
        # return helper(0, 0, 0, sum(nums))