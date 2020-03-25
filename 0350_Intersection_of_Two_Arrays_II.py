# Runtime: 44 ms, faster than 81.14% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 13.1 MB, less than 88.57% of Python3 online submissions for Intersection of Two Arrays II.

from collections import defaultdict, Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # d1, d2 = defaultdict(int), defaultdict(int)
        # for num in nums1:
        #     d1[num] += 1
        # for num in nums2:
        #     d2[num] += 1
        # ans = []
        # for k, v in d1.items():
        #     if k in d2:
        #         ans.extend([k] * min(v, d2[k]))
        # return ans
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return (c1 & c2).elements()