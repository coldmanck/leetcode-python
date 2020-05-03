# a.k.a. Search for a Range

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Two-pass binary search O(logn)
        # ALWAYS REMEMBER TO CHECK CORNER CASES!
        if not nums:
            return -1, -1
        
        # find start
        left, right = 0, len(nums) - 1
        start = -1 # as a flag for later check
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target and nums[mid - 1] < target:
                start = mid
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if start == -1:
            if nums[left] == target:
                start = left
            else:
                return -1, -1
        
        # find end
        left, right = start, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target and nums[mid + 1] > target:
                return start, mid
            if nums[mid] == target:
                left = mid + 1
            else:
                right = mid - 1
        return start, left