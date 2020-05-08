class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''time O(n) space O(1)'''
        nums.reverse()
        k %= len(nums)
        
        left, right = 0, k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
        
        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
            
        
        '''time = space = O(n)'''
        # nums2 = nums[:]
        # k %= len(nums)
        # nums[:k] = nums2[len(nums) - k:]
        # nums[k:] = nums2[:len(nums) - k]