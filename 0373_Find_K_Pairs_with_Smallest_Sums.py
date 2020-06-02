class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''priority queue: time O(k+(n-k)logk) space O(k)'''
        if k >= len(nums1) * len(nums2):
            return [[i, j] for i in nums1 for j in nums2]
        nums = [(-(i + j), i, j) for i in nums1 for j in nums2]
        import heapq
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if -nums[i][0] < -heap[0][0]:
                heapq.heapreplace(heap, nums[i])
        return [num[1:] for num in heap]
        