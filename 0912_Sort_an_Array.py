# Runtime: 280 ms, faster than 70.79% of Python3 online submissions for Sort an Array.
# Memory Usage: 19.7 MB, less than 57.14% of Python3 online submissions for Sort an Array.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quicksort time O(nlogn) space O(1) (in-place)
        def partition(left, right, nums):
            pivot = nums[right]
            new_pivot_idx = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                    new_pivot_idx += 1
            nums[new_pivot_idx], nums[right] = nums[right], nums[new_pivot_idx]
            return new_pivot_idx
        
        def quicksort(left, right, nums):
            if left < right:
                pivot_idx = partition(left, right, nums)
                quicksort(left, pivot_idx - 1, nums)
                quicksort(pivot_idx + 1, right, nums)
        
        quicksort(0, len(nums) - 1, nums)
        return nums