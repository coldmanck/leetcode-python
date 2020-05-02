import heapq
class KthLargest:
    '''
    Time: 
        __init__: O(k + (n-k)logk)
        add: O(logk)
    Space: O(k) for the heap
    '''
    def __init__(self, k: int, nums: List[int]):
        # (1) build a min heap of size k (for storing the top-k largest elements)
        # (2) compare the root with nums[k:n]:
        #   if the root.val smaller than the num[i]: replace with the num[i]
        def build_heap(k, nums):
            heap = nums[:k]
            heapq.heapify(heap)
            for i in range(k, len(nums)):
                if heap[0] < nums[i]:
                    heapq.heapreplace(heap, nums[i])
            return heap
        
        self.heap = build_heap(k, nums)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)