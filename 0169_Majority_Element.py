# Runtime: 192 ms, faster than 24.18% of Python3 online submissions for Majority Element.
# Memory Usage: 14.3 MB, less than 97.62% of Python3 online submissions for Majority Element.

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > (len(nums) // 2):
                return num