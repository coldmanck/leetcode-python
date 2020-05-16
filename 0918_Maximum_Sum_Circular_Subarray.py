import heapq
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # kadane algorithm with heap storing the minimum elements
        length = len(A)
        A.extend(A[:-1])
        max_sum = float('-inf')
        min_cum_sum = [(0, -1)] # min_cum_Sum, idx
        cur_cum_sum = 0
        for i in range(len(A)):
            if i > 0:
                while i - min_cum_sum[0][1] > length: # if the minimum element's idx is farther than length than pop out
                    heapq.heappop(min_cum_sum)
                heapq.heappush(min_cum_sum, (cur_cum_sum, i - 1)) # note here is i - 1   
            cur_cum_sum += A[i]
            max_sum = max(max_sum, cur_cum_sum - min_cum_sum[0][0])
        return max_sum
        
        '''TLE solution: naive kadane algorithm * n times O(n^2)'''
        # max_sum = float('-inf')
        # for i in range(len(A)):
        #     min_cum_sum = cur_cum_sum = 0
        #     for num in A[i:] + A[:i]:
        #         min_cum_sum = min(min_cum_sum, cur_cum_sum)
        #         cur_cum_sum += num
        #         max_sum = max(max_sum, cur_cum_sum - min_cum_sum)
        # return max_sum