class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        
        if not nums:
            return
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            reverse(nums, 0, len(nums) - 1)
            return
        
        # a) another pass to find the smallest number after idx (i-1) that larger than nums[i - 1]
        # j = i
        # while j < len(nums) and nums[j] > nums[i - 1]:
        #     j += 1
        
        # a-2) can use binary search instead
        left, right = i, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] <= nums[i - 1]:
                right = mid - 1
            else:
                left = mid
        j = left + 1
        
        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
        reverse(nums, i, len(nums) - 1)
        return