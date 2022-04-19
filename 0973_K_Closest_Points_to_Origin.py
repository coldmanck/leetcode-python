class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def comp_dist(point):
            return point[0] ** 2 + point[1] ** 2
        import heapq
        
        '''solution 1: heap
        time O(N + klogN)
        space O(N)
        '''
        # heap = [(comp_dist(point), point) for point in points]
        # heapq.heapify(heap)
        # ans = []
        # while len(ans) < k:
        #     dist, point = heapq.heappop(heap)
        #     ans.append(point)
        # return ans
        
        '''solution 2: optimized heap
        time O(k + (N-k)logk)
        space O(k)
        '''
        # heap = [(-comp_dist(point), point) for point in points[:k]]
        # heapq.heapify(heap) # max heap
        # ans = []
        # for point in points[k:]:
        #     dist = -comp_dist(point)
        #     if dist > heap[0][0]:
        #         heapq.heappushpop(heap, (dist, point))
        # return [point for dist, point in heap]
        
        '''Quickselect: time best=avg=O(n) worst=O(n^2) space O(n)'''
        if K == len(points):
            return points
        
        def partition(left, right):
            # Optional: median-of-median
            pivot_idx = sorted([(points[left], left), (points[right], right), (points[(left + right) // 2], (left + right) // 2)])[1][1]
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            
            pivot = points[right][0] ** 2 + points[right][1] ** 2
            cur_pivot_idx = left
            for i in range(left, right):
                if points[i][0] ** 2 + points[i][1] ** 2 <= pivot:
                    points[cur_pivot_idx], points[i] = points[i], points[cur_pivot_idx]
                    cur_pivot_idx += 1
            points[cur_pivot_idx], points[right] = points[right], points[cur_pivot_idx]
            return cur_pivot_idx
        
        left, right = 0, len(points) - 1
        while left <= right:
            pivot_idx = partition(left, right)
            if pivot_idx == K - 1:
                break
            elif pivot_idx < K - 1:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1
        
        return points[:K]