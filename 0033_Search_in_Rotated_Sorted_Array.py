class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Method 1: One-pass binary search
        # Time complexity : O(logN), Space complexity : O(1)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        return left if nums[left] == target else -1
        
        # Method 2: Two-pass binary search
        # Time complexity : O(logN), Space complexity : O(1)
        # find out the start in O(logn) time
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        if target > nums[-1]:
            left, right = 0, pivot
        else:
            left, right = pivot, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left if nums[left] == target else -1
        '''