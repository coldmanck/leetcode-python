class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans