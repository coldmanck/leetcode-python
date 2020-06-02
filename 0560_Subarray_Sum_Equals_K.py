class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # time O(n) space O(n)
        from collections import defaultdict
        to_find = defaultdict(int)
        cum = ans = 0
        for num in nums:
            if num == k:
                ans += 1
            cum += num
            ans += to_find[cum]
            to_find[cum - num + k] += 1
        return ans