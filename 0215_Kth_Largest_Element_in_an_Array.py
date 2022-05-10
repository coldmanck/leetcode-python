import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time complexity: O(k + (n - k)logk) = O(nlogk)
        # space complexity: O(k)
        if len(nums) <= k:
            return min(nums)
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
        return heap[0]