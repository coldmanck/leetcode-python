class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''Brute-force recursion (TLE): time O(2^n) space O(n)'''
        def max_lis(idx, cur_max):
            if idx == len(nums):
                return 0
            if nums[idx] > cur_max:
                return max(1 + max_lis(idx + 1, nums[idx]), max_lis(idx + 1, cur_max))
            return max_lis(idx + 1, cur_max)
        return max_lis(0, float('-inf'))
    
        '''Recursion with memoization (DP): time O(n^2) space O(n^2)
        - memo[i][j] represents the length of the LIS possible using nums[i] as 
          the previous element considered to be included/not included in the LIS, with 
          nums[j] as the current element considered to be included/not included in the LIS.
        '''
        from collections import defaultdict
        cache = defaultdict(dict) # 2D cache of prev_max_idx & cur_idx
        nums.append(float('-inf'))
        def max_lis(idx, prev_max_idx):
            if idx == len(nums) - 1:
                return 0
            if prev_max_idx not in cache or idx not in cache[prev_max_idx]:
                if nums[idx] > nums[prev_max_idx]:
                    cache[prev_max_idx][idx] = max(1 + max_lis(idx + 1, idx), max_lis(idx + 1, prev_max_idx))
                else:
                    cache[prev_max_idx][idx] = max_lis(idx + 1, prev_max_idx)
            return cache[prev_max_idx][idx]
        return max_lis(0, -1)
        
        '''Bottom-up DP: time O(n^2) space O(n)'''
        if not nums:
            return 0
        dp = [1] * len(nums)
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])
        return max_len
        
        '''Bottom-up DP + binary-search: time O(nlogn) space O(n). (patience sorting)'''
        if not nums:
            return 0
        dp = [nums[0]]
        len_dp = 1
        for i in range(1, len(nums)):
            left, right = 0, len(dp) - 1
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if dp[left] < nums[i]:
                dp.append(nums[i])
                len_dp += 1
            else:
                dp[left] = nums[i]
        return len_dp