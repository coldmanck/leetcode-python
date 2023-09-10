class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''time O(n) space O(1)'''
        nums.reverse()
        k %= len(nums)
        def reverse_(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
        reverse_(nums, 0, k - 1)
        reverse_(nums, k, len(nums) - 1)
            
        
        '''time = space = O(n)'''
        # nums2 = nums[:]
        # k %= len(nums)
        # nums[:k] = nums2[len(nums) - k:]
        # nums[k:] = nums2[:len(nums) - k]