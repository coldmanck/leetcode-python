class Solution:
    # time complexity: worst O(n), avg=best=O(logn)
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            new_mid = mid
            while nums[new_mid] == nums[right]:
                new_mid -= 1
                if new_mid == mid or nums[new_mid] > nums[new_mid + 1]:
                    return nums[new_mid + 1]
                if new_mid < 0:
                    new_mid = len(nums) - 1
            if nums[new_mid] > nums[right]:
                left = new_mid + 1
            else:
                right = new_mid
        return nums[left]
                