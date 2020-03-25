# Runtime: 52 ms, faster than 64.11% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 13.5 MB, less than 76.74% of Python3 online submissions for Trapping Rain Water.

class Solution:
    def trap(self, height: List[int]) -> int:
        '''Method 1 brute force (TLE) O(n^2) time O(1) space'''
        # total = 0
        # for i in range(len(height)):
        #     max_left = max_right = 0
        #     for j in range(i, -1, -1):
        #         max_left = max(max_left, height[j])
        #     for j in range(i, len(height)):
        #         max_right = max(max_right, height[j])
        #     total += min(max_left, max_right) - height[i]
        # return total
        
        '''Method 2 DP: O(n) time O(n) space'''
        max_lefts, max_rights = [0] * len(height), [0] * len(height)
        max_left = max_right = 0
        for i in range(len(height)):
            max_left = max(max_left, height[i])
            max_lefts[i] = max_left
        for i in reversed(range(len(height))):
            max_right = max(max_right, height[i])
            max_rights[i] = max_right
        total = 0
        for i in range(len(height)):
            total += min(max_lefts[i], max_rights[i]) - height[i]
        return total