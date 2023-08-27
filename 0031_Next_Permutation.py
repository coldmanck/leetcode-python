class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        # i: find nums[i] that is smaller than nums[i+1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            nums.reverse()
            return
        # j: find nums[j] that is larger than nums[i]
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        # swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        # reverse nums[i+1:] so that the remaining transforms from non-increasing to non-decreasing
        nums[i+1:] = reversed(nums[i+1:])