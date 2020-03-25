# Easy
# Runtime: 76 ms, faster than 97.11% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.5 MB, less than 98.36% of Python3 online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if nums[idx] != num:
                idx += 1
                nums[idx] = num
        return idx + 1