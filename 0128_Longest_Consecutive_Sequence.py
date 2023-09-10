class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nums = set(nums)
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best