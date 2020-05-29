class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(idx, nums, cache): # this function is the same as that in 198. House Robber
            if idx >= len(nums):
                return 0
            if idx == len(nums) - 1:
                return nums[-1]
            if idx not in cache:
                cache[idx] = max(nums[idx] + helper(idx + 2, nums, cache), nums[idx + 1] + helper(idx + 3, nums, cache))
            return cache[idx]
        return max(helper(0, nums[1:], {}), helper(0, nums[:-1], {}))