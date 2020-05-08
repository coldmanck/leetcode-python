class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''brute-force + binary-search: time O(nlogn) space O(n)'''
        if not nums:
            return 0
        # create a cumulative sum array (time O(n) space O(n) here)
        cum = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            cum[i] = cum[i - 1] + nums[i]
        # for each idx, find the least farthest ending idx using binary search
        min_len = float('inf')
        for i in range(len(nums)):
            left, right = i, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if cum[mid] - cum[i] + nums[i] < s:
                    left = mid + 1
                else:
                    right = mid
            if cum[left] - cum[i] + nums[i] >= s:
                min_len = min(min_len, left - i + 1)
            else:
                break
        return 0 if min_len == float('inf') else min_len
        
        '''Two-pointers method: time O(n) space O(1)'''
#         if not nums:
#             return 0
        
#         left = right = cur_sum = 0
#         min_len = float('inf')
#         while right < len(nums):
#             cur_sum += nums[right]
#             while cur_sum >= s:
#                 min_len = min(min_len, right - left + 1)
#                 cur_sum -= nums[left]
#                 left += 1
#             right += 1
        
#         return 0 if min_len == float('inf') else min_len
            