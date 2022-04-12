# Runtime: 40 ms, faster than 91.18% of Python3 online submissions for Find Peak Element.
# Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Find Peak Element.

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] > nums[mid - 1] and nums[mid] > nums[(mid + 1)]:
#                 return mid
#             if nums[mid] < nums[mid + 1]: # ascending slope
#                 left = mid + 1
#             else: # descending slope
#                 right = mid - 1
            
#         return left

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] or mid - 1 < 0:
                if nums[(mid + 1) % len(nums)] < nums[mid] or mid + 1 > len(nums) - 1:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1
        

if __name__ == '__main__':
    nums = [1,2,3] # [5,4,3,2,1]
    sol = Solution()
    print(sol.findPeakElement(nums))