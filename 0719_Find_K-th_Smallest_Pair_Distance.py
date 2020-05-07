class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Time: n * log(n) * log(max - min)
        def lowerest_idx_greater_than(target, left):
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2 + 1
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid
            return left + 1
        
        def n_pairs_lower_than(mid):
            ans = 0
            for i in range(len(nums)):
                ans += lowerest_idx_greater_than(nums[i] + mid, i) - i - 1
            return ans
        
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if n_pairs_lower_than(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
        
        # create a max heap of size k with nums[:k], then compare each num in nums[k:]
        # with the heap[0] and replace if heap[0] is larger than the num. Return the heap top.
        # time O(k) + O((n*n-k)(logk)) space O(k)
        '''
        import heapq
        heap = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                dist = abs(nums[j] - nums[i])
                if len(heap) < k:
                    heapq.heappush(heap, -dist)
                elif -heap[0] > dist:
                    heapq.heapreplace(heap, -dist)
        return -heap[0]
        '''
        
        # Method 2: sort the array and computing dist. of neighboring elements. 
        # Still maintain a max heap of size k.
        # time O(nlogn + k + nlogk)
        '''
        import heapq
        heap = []
        nums.sort()
        print(nums)
        for i in range(1, len(nums)):
            dist = abs(nums[i] - nums[i - 1])
            print(i, dist)
            if len(heap) < k:
                heapq.heappush(heap, -dist)
            elif -heap[0] > dist:
                heapq.heapreplace(heap, -dist)
        return -heap[0]
        '''