class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {} # key of idx, value of max_money_can_steal
        def helper(idx):
            if idx >= len(nums):
                return 0
            if idx == len(nums) - 1:
                return nums[-1]
            if idx not in cache:
                cache[idx] = max(nums[idx] + helper(idx + 2), nums[idx + 1] + helper(idx + 3))
            return cache[idx]
        return helper(0)