class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''Floyd's tortoise and hare algorithm (cycle detection), works in Time O(n) Space O(1)'''
        if 1 <= len(nums) <= 2:
            return nums[0]
        fast, slow = nums[nums[nums[0]]], nums[nums[0]]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast
        
        '''(doesn't work for restriction) Method 1 in-place sorting O(nlogn) time O(1) space'''
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        '''(doesn't work for restriction) Method 2 useing set: O(n) time O(n) space'''
        # myset = set()
        # for num in nums:
        #     if num in myset:
        #         return num
        #     myset.add(num)