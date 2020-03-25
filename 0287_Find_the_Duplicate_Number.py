# Runtime: 64 ms, faster than 83.94% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 17.9 MB, less than 7.14% of Python3 online submissions for Find the Duplicate Number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''Method 1 in-place sorting O(nlogn) time O(1) space'''
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        '''Method 2 useing set: O(n) time O(n) space'''
        myset = set()
        for num in nums:
            if num in myset:
                return num
            myset.add(num)