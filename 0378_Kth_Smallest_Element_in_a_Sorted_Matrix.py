# Runtime: 228 ms, faster than 40.25% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 18.8 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''Method 1: use pointer
        Time: O(kn)
        Spce: O(n)'''
        # n = len(matrix)
        # ids = [0] * n
        # min_row = -1
        # while k:
        #     ans = (float('inf'), -1)
        #     for row in range(n):
        #         if ids[row] >= n:
        #             continue
        #         if (matrix[row][ids[row]], row) < ans:
        #             min_row = row
        #             ans = (matrix[row][ids[row]], row)
        #     # print(min_row, k, ids, ans)
        #     ids[min_row] += 1
        #     k -= 1
        # return ans[0]
        
        '''Method 2: use min-heap
        Time: O(min(n, k)) heapify + O(klogn) heap pop
        Spce: O(min(n, k))'''
        heap = []
        for row in range(min(k, len(matrix))):
            # matrix[row].reverse()
            # heappush(heap, (matrix[row].pop(), row))
            heappush(heap, (matrix[row][0], row, 0))
        while k:
            num = heappop(heap)
            # if matrix[num[1]]:
            #     heappush(heap, (matrix[num[1]].pop(), num[1]))
            if num[2] != len(matrix) - 1:
                heappush(heap, (matrix[num[1]][num[2] + 1], num[1], num[2] + 1))
            k -= 1
        return num[0]