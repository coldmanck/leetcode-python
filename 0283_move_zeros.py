# Runtime: 44 ms, faster than 90.86% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Move Zeroes.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute-force O(n^2)
        '''
        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                for j in range(i, len(nums)-1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        '''
        
        # use deque: O(n) time O(n) space
        '''
        from collections import deque
        zero_idxs = deque()
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idxs.append(i)
            elif len(zero_idxs) > 0:
                zero_idx = zero_idxs.popleft()
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idxs.append(i)
        return nums
        '''
        
        '''O(n) time O(1) space method'''
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        nums[j:] = [0] * (len(nums) - j)