# Runtime: 280 ms, faster than 70.79% of Python3 online submissions for Sort an Array.
# Memory Usage: 19.7 MB, less than 57.14% of Python3 online submissions for Sort an Array.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort: avg, worst, best time = O(nlogn), space = O(n)
        def mergesort(left, right, nums):
            if left < right:
                pivot = (left + right) // 2
                mergesort(left, pivot, nums)  # divide & conquer
                mergesort(pivot + 1, right, nums) # divide & conquer
                nums[left:right + 1] = merge(left, pivot, right, nums) # combine 
        
        def merge(left, pivot, right, nums):
            ans = []
            right_s = pivot + 1
            while left <= pivot and right_s <= right:
                if nums[left] <= nums[right_s]:
                    ans.append(nums[left])
                    left += 1
                else:
                    ans.append(nums[right_s])
                    right_s += 1
            if left <= pivot:
                ans.extend(nums[left:pivot+1])
            else:
                ans.extend(nums[right_s:right+1])
            return ans
        
        mergesort(0, len(nums) - 1, nums)
        return nums
            
        # quicksort: best, avg time O(nlogn), worst time O(n^2), space = O(1)
        '''
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
                pivot_idx = partition(left, right, nums) # divide
                quicksort(left, pivot_idx - 1, nums) # conquer
                quicksort(pivot_idx + 1, right, nums) # conquer
        
        quicksort(0, len(nums) - 1, nums)
        return nums
        '''