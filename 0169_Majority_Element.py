# Runtime: 192 ms, faster than 24.18% of Python3 online submissions for Majority Element.
# Memory Usage: 14.3 MB, less than 97.62% of Python3 online submissions for Majority Element.

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''Sorting time O(nlogn) space O(1)'''
        if len(nums) == 1:
            return nums[0]
        count = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count > len(nums) // 2:
                return nums[i]
        
        '''hashmap time O(n) space O(1)'''
        # counter = defaultdict(int)
        # for num in nums:
        #     counter[num] += 1
        #     if counter[num] > (len(nums) // 2):
        #         return num