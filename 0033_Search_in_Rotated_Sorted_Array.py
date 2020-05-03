class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Method 1: One-pass binary search
        # Time complexity : O(logN), Space complexity : O(1)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
        
        # Method 2: Two-pass binary search
        # Time complexity : O(logN), Space complexity : O(1)
        # find out the start in O(logn) time
        '''
        left, right = 0, len(nums) - 1
        start = None
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[mid - 1]:
                start = mid
                break
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        if start is None:
            return -1

        nums = nums[start:] + nums[:start]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return (mid + start) % len(nums)
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        '''