# Runtime: 136 ms, faster than 43.07% of Python3 online submissions for Container With Most Water.
# Memory Usage: 15.3 MB, less than 5.26% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans