# Runtime: 136 ms, faster than 21.64% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.3 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''linaer scanning: time O(n) space O(n)'''
        # my_set = set()
        # for num in nums:
        #     if num in my_set:
        #         return True
        #     my_set.add(num)
        # return False
        
        '''scan after sorting: time O(nlogn) space O(1)'''
        for i, num in enumerate(sorted(nums)):
            if i != 0 and num == old_num:
                return True
            old_num = num
        return False
            