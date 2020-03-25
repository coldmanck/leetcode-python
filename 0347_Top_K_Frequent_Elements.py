# Runtime: 112 ms, faster than 33.23% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 17.4 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.

from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. use a defaultdict(int) to count each num's occurrence (O(n))
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        # 2. Build a max heap using (freq, num) (O(m) where m is the number of different number)
        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)
        
        # 3. Output k times
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans