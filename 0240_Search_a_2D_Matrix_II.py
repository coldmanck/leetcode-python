# Runtime: 40 ms, faster than 32.96% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 18.7 MB, less than 7.41% of Python3 online submissions for Search a 2D Matrix II.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Method 1: time O(m + n)
        if not matrix or not matrix[0]:
            return False
        idx = len(matrix[0]) - 1
        for row in matrix:
            while idx > 0 and row[idx] > target:
                idx -= 1
            if row[idx] == target:
                return True
        return False
        
        # Method 2: time min(O(mlogn), O(nlogm))
#         def binary_search(nums, target):
#             left, right = 0, len(nums) - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     return True
#                 if nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return False
        
#         if not matrix or not matrix[0]:
#             return False
#         col_idx = row_idx = 0
        
#         if len(matrix) > len(matrix[0]):
#             while col_idx < len(matrix[0]):
#                 if binary_search([matrix[i][col_idx] for i in range(len(matrix))], target):
#                     return True
#                 col_idx += 1
#         else:
#             while row_idx < len(matrix):
#                 if binary_search(matrix[row_idx], target):
#                     return True
#                 row_idx += 1
        
#         return False

if __name__ == '__main__':
    a = [[1,   4,  7, 11, 15],
         [2,   5,  8, 12, 19],
         [3,   6,  9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]
    sol = Solution()
    print(sol.searchMatrix(a, 5))
    