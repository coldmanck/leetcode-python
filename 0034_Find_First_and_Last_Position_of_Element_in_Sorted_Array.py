# a.k.a. Search for a Range

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1, -1
        
        # bisect_left
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if not nums[left] == target:
            return -1, -1
        start = left
        
        # bisect_right
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return start, left
        
        # Two-pass binary search O(logn)
        # ALWAYS REMEMBER TO CHECK CORNER CASES!
        '''
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
                right = mid
        
        if start == -1:
            if nums[left] == target:
                start = left
            else:
                return -1, -1
        
        # find end
        left, right = start, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            print(left, mid, right)
            if nums[mid] == target and nums[mid + 1] > target:
                return start, mid
            if nums[mid] == target:
                left = mid + 1
            else:
                right = mid
        return start, left
        '''